// unsubscribe: GET (link in every email) or POST (RFC 8058 one-click List-Unsubscribe-Post).
// Marks the subscriber unsubscribed, withdraws all four consents, appends a consent event.
// Deploy with --no-verify-jwt. The unsubscribe token stays valid so repeated clicks are harmless.
import { admin, redirect, sha256hex } from "../_shared/util.ts";

Deno.serve(async (req) => {
  if (req.method !== "GET" && req.method !== "POST") return new Response("method not allowed", { status: 405 });
  const token = new URL(req.url).searchParams.get("token") ?? "";
  if (!/^[A-Za-z0-9_-]{40,64}$/.test(token)) return redirect("?subscribed=invalid");
  const db = admin();
  const { data: sub } = await db.from("subscribers").select("id,status,locale")
    .eq("unsubscribe_token_hash", await sha256hex(token)).maybeSingle();
  if (!sub) return req.method === "POST" ? new Response("ok") : redirect("?subscribed=invalid");
  if (sub.status !== "unsubscribed") {
    await db.from("subscribers").update({
      status: "unsubscribed", unsubscribed_at: new Date().toISOString(),
      consent_product_updates: false, consent_promotions: false, consent_beta_invites: false, consent_research: false,
      confirm_token_hash: null, confirm_token_expires_at: null,
    }).eq("id", sub.id);
    await db.from("consent_events").insert({
      subscriber_id: sub.id, event: "unsubscribed",
      consents: { product_updates: false, promotions: false, beta_invites: false, research: false },
    });
  }
  return req.method === "POST" ? new Response("ok") : redirect("?subscribed=unsubscribed", sub.locale);
});
