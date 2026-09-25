// confirm: GET /confirm?token=… from the confirmation email. Validates the token (by its SHA-256 hash,
// unexpired, still pending), marks the subscriber confirmed, appends a consent event, and redirects
// to the site with ?subscribed=confirmed (or =invalid). Deploy with --no-verify-jwt (it is a public link).
import { admin, consentsOf, redirect, sha256hex } from "../_shared/util.ts";

Deno.serve(async (req) => {
  const token = new URL(req.url).searchParams.get("token") ?? "";
  if (!/^[A-Za-z0-9_-]{40,64}$/.test(token)) return redirect("?subscribed=invalid");
  const db = admin();
  const hash = await sha256hex(token);
  const { data: sub } = await db.from("subscribers")
    .select("id,status,locale,confirm_token_expires_at,consent_product_updates,consent_promotions,consent_beta_invites,consent_research,consent_text_version")
    .eq("confirm_token_hash", hash).maybeSingle();
  if (!sub) return redirect("?subscribed=invalid");
  if (sub.status !== "pending" || !sub.confirm_token_expires_at || new Date(sub.confirm_token_expires_at) < new Date()) {
    return redirect("?subscribed=invalid", sub.locale);
  }
  const { error } = await db.from("subscribers").update({
    status: "confirmed", confirmed_at: new Date().toISOString(),
    confirm_token_hash: null, confirm_token_expires_at: null,
  }).eq("id", sub.id).eq("status", "pending");
  if (error) return new Response("error", { status: 500 });
  await db.from("consent_events").insert({
    subscriber_id: sub.id, event: "confirmed", consents: consentsOf(sub), consent_text_version: sub.consent_text_version,
  });
  return redirect("?subscribed=confirmed", sub.locale);
});
