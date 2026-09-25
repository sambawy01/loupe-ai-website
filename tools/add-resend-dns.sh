#!/bin/zsh
# Adds Resend's four sending records to loupe-ai.com at GoDaddy. PATCH adds; it never replaces other records.
: ${GODADDY_KEY:?set GODADDY_KEY} ${GODADDY_SECRET:?set GODADDY_SECRET}
curl -sS -w '\nHTTP %{http_code}\n' -X PATCH "https://api.godaddy.com/v1/domains/loupe-ai.com/records" \
  -H "Authorization: sso-key $GODADDY_KEY:$GODADDY_SECRET" -H "Content-Type: application/json" -d '[
 {"type":"TXT","name":"resend._domainkey","data":"p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC2DlW4P1gL0BhZ+z276Y/w6loXFHsIVn8AcLy9OOredVIxn5OBxGWKYXl43qFUXi/jzCj2AF4oYnrnWjLQ1HwIvsfr14Kf3IFZ117MvZ30Tv2tp5h2EFm6d/NwgGLPvCUYXDQ4gntHPId93eHC07sFBXH+GZzd0H9YISjwxT/YCwIDAQAB","ttl":600},
 {"type":"MX","name":"send","data":"feedback-smtp.eu-west-1.amazonses.com","priority":10,"ttl":600},
 {"type":"TXT","name":"send","data":"v=spf1 include:amazonses.com ~all","ttl":600},
 {"type":"CNAME","name":"rsend","data":"send.forge.rmta.net","ttl":600}]'
