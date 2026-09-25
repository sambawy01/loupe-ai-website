/* Site configuration. PLACEHOLDERS — replace before launch (see README.md).
   The anon key is public by design (RLS allows INSERT only). Never put a service-role key here. */
window.LOUPE_CONFIG = {
  SUPABASE_URL: "https://YOUR-PROJECT-REF.supabase.co",      // TODO: Supabase project URL
  SUPABASE_ANON_KEY: "YOUR-SUPABASE-ANON-KEY",               // TODO: Supabase anon (public) key

  // Loupe Station for Mac: the latest release in the public downloads repo.
  MAC_RELEASES_API: "https://api.github.com/repos/sambawy01/loupe-downloads/releases/latest",
  MAC_DOWNLOAD_URL: "https://github.com/sambawy01/loupe-downloads/releases/latest", // TODO: or https://loupe-ai.com/download/LoupeStation.dmg
  MAC_AVAILABLE: false,       // TODO: false = "coming soon"; null = ask the GitHub API for the latest release
                              // (use once sambawy01/loupe-downloads is public and has a .dmg); true = always link MAC_DOWNLOAD_URL

  // Loupe for iPhone (com.loupe-ai.ios). Not yet on the App Store.
  APP_STORE_URL: "https://apps.apple.com/app/idPLACEHOLDER", // TODO: real App Store URL once published
  IOS_AVAILABLE: false,       // TODO: set true once the app is live on the App Store

  CONSENT_TEXT_VERSION: "2026-09-25.v1"
};
