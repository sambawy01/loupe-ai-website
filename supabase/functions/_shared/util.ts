// Shared helpers for the loupe-ai.com Edge Functions (Deno).
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.45.4";

// Service-role client. SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY are injected by Supabase at runtime;
// they are never in this repository.
export function admin() {
  const url = Deno.env.get("SUPABASE_URL");
  const key = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
  if (!url || !key) throw new Error("missing SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY");
  return createClient(url, key, { auth: { persistSession: false } });
}

export const SITE = Deno.env.get("SITE_URL") ?? "https://loupe-ai.com";

export function randomToken(bytes = 32): string {
  const b = crypto.getRandomValues(new Uint8Array(bytes));
  return btoa(String.fromCharCode(...b)).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

export async function sha256hex(s: string): Promise<string> {
  const d = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return [...new Uint8Array(d)].map((x) => x.toString(16).padStart(2, "0")).join("");
}

export function timingSafeEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let r = 0;
  for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}

export function redirect(path: string, locale = "en"): Response {
  const base = locale === "ar" ? `${SITE}/ar/` : `${SITE}/`;
  return new Response(null, { status: 303, headers: { Location: base + path, "Cache-Control": "no-store" } });
}

export function consentsOf(row: Record<string, unknown>) {
  return {
    product_updates: !!row.consent_product_updates,
    promotions: !!row.consent_promotions,
    beta_invites: !!row.consent_beta_invites,
    research: !!row.consent_research,
  };
}
