#!/bin/zsh
# Puts loupe-ai.com live on GitHub Pages and adds Resend's email records, via the GoDaddy API.
# Token: first argument is a file holding the GoDaddy PAT (Bearer). The token is never printed.
set -e
T=$(<"$1")
API=https://api.godaddy.com/v1/domains/loupe-ai.com/records
H=(-H "Authorization: Bearer $T" -H "Content-Type: application/json")
echo "== before"; curl -s "${H[@]}" $API | python3 -c "import json,sys;[print(r['type'],r['name'],r['data'][:70]) for r in json.load(sys.stdin)]"
# Apex -> GitHub Pages (replaces the parking A records only).
curl -sf -o /dev/null -w "A @ %{http_code}\n" -X PUT "${H[@]}" $API/A/@ -d '[{"data":"185.199.108.153","ttl":600},{"data":"185.199.109.153","ttl":600},{"data":"185.199.110.153","ttl":600},{"data":"185.199.111.153","ttl":600}]'
curl -sf -o /dev/null -w "CNAME www %{http_code}\n" -X PUT "${H[@]}" $API/CNAME/www -d '[{"data":"sambawy01.github.io","ttl":600}]'
# Resend sending records (subdomains only).
curl -sf -o /dev/null -w "Resend %{http_code}\n" -X PATCH "${H[@]}" $API -d '[
 {"type":"TXT","name":"resend._domainkey","data":"p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC2DlW4P1gL0BhZ+z276Y/w6loXFHsIVn8AcLy9OOredVIxn5OBxGWKYXl43qFUXi/jzCj2AF4oYnrnWjLQ1HwIvsfr14Kf3IFZ117MvZ30Tv2tp5h2EFm6d/NwgGLPvCUYXDQ4gntHPId93eHC07sFBXH+GZzd0H9YISjwxT/YCwIDAQAB","ttl":600},
 {"type":"MX","name":"send","data":"feedback-smtp.eu-west-1.amazonses.com","priority":10,"ttl":600},
 {"type":"TXT","name":"send","data":"v=spf1 include:amazonses.com ~all","ttl":600},
 {"type":"CNAME","name":"rsend","data":"send.forge.rmta.net","ttl":600}]'
echo "== after"; curl -s "${H[@]}" $API | python3 -c "import json,sys;[print(r['type'],r['name'],r['data'][:70]) for r in json.load(sys.stdin)]"
