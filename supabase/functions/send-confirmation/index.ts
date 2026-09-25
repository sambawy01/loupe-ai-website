// send-confirmation: called by a Supabase Database Webhook on INSERT into public.subscribers.
// Generates the confirm + unsubscribe tokens, stores only their SHA-256 hashes, and emails the
// double opt-in link through Resend.
//
// Secrets (set with `supabase secrets set ...`, never committed):
//   RESEND_API_KEY   TODO: your Resend API key
//   WEBHOOK_SECRET   TODO: a long random string; put the same value in the webhook's
//                    "Authorization: Bearer <WEBHOOK_SECRET>" header
//   MAIL_FROM        e.g. "Loupe <hello@loupe-ai.com>" (domain verified in Resend)
//   FUNCTIONS_URL    e.g. https://<project-ref>.functions.supabase.co
import { admin, randomToken, sha256hex, timingSafeEqual } from "../_shared/util.ts";

const T = {
  en: {
    subject: "Confirm your Loupe sign-up",
    body: (c: string, u: string) =>
      `<p>Hi,</p><p>Someone (hopefully you) asked to hear about Loupe at this address. Confirm with the link below — until you do, we won't email you anything else.</p>` +
      `<p><a href="${c}">Confirm my sign-up</a></p><p>The link works for 7 days. If this wasn't you, ignore this email and nothing more will be sent.</p>` +
      `<p style="color:#666;font-size:12px">Changed your mind? <a href="${u}">Unsubscribe</a>. · Loupe, Hurghada, Egypt · privacy@loupe-ai.com</p>`,
  },
  ar: {
    subject: "أكّد تسجيلك في Loupe",
    body: (c: string, u: string) =>
      `<div dir="rtl"><p>مرحبًا،</p><p>طلب أحدٌ (نأمل أن تكون أنت) أن يسمع عن Loupe على هذا العنوان. أكّد بالرابط أدناه — ولن نراسلك بشيء آخر قبل ذلك.</p>` +
      `<p><a href="${c}">تأكيد التسجيل</a></p><p>الرابط صالح 7 أيام. إن لم تكن أنت فتجاهل هذه الرسالة ولن يُرسل شيء آخر.</p>` +
      `<p style="color:#666;font-size:12px">غيّرت رأيك؟ <a href="${u}">إلغاء الاشتراك</a> · Loupe، الغردقة، مصر · privacy@loupe-ai.com</p></div>`,
  },
};

Deno.serve(async (req) => {
  if (req.method !== "POST") return new Response("method not allowed", { status: 405 });
  const secret = Deno.env.get("WEBHOOK_SECRET") ?? "";
  const auth = req.headers.get("authorization") ?? "";
  if (!secret || !timingSafeEqual(auth, `Bearer ${secret}`)) return new Response("unauthorized", { status: 401 });

  const payload = await req.json().catch(() => null);
  const rec = payload?.record;
  if (payload?.type !== "INSERT" || payload?.table !== "subscribers" || !rec?.id) {
    return new Response("ignored", { status: 200 });
  }

  const db = admin();
  const { data: sub, error } = await db.from("subscribers")
    .select("id,email,language,status,confirmation_sent_at").eq("id", rec.id).single();
  if (error || !sub || sub.status !== "pending" || sub.confirmation_sent_at) return new Response("skip", { status: 200 });

  const confirmToken = randomToken();
  const unsubToken = randomToken();
  const { error: upErr } = await db.from("subscribers").update({
    confirm_token_hash: await sha256hex(confirmToken),
    confirm_token_expires_at: new Date(Date.now() + 7 * 24 * 3600 * 1000).toISOString(),
    unsubscribe_token_hash: await sha256hex(unsubToken),
    confirmation_sent_at: new Date().toISOString(),
  }).eq("id", sub.id).is("confirmation_sent_at", null);
  if (upErr) return new Response("db error", { status: 500 });

  const fn = Deno.env.get("FUNCTIONS_URL"); // TODO: set as a secret
  const confirmUrl = `${fn}/confirm?token=${confirmToken}`;
  const unsubUrl = `${fn}/unsubscribe?token=${unsubToken}`;
  const lang = sub.language === "ar" ? "ar" : "en";

  const key = Deno.env.get("RESEND_API_KEY"); // TODO: `supabase secrets set RESEND_API_KEY=...`
  if (!key) return new Response("RESEND_API_KEY not set", { status: 500 });
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from: Deno.env.get("MAIL_FROM") ?? "Loupe <hello@loupe-ai.com>",
      to: [sub.email],
      subject: T[lang].subject,
      html: T[lang].body(confirmUrl, unsubUrl),
      headers: { "List-Unsubscribe": `<${unsubUrl}>`, "List-Unsubscribe-Post": "List-Unsubscribe=One-Click" },
    }),
  });
  if (!r.ok) {
    // allow a retry by clearing the sent marker
    await db.from("subscribers").update({ confirmation_sent_at: null }).eq("id", sub.id);
    return new Response("send failed", { status: 502 });
  }
  return new Response("sent", { status: 200 });
});
