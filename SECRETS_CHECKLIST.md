# GitHub Secrets Checklist

## Required Secrets (Add all 5)

Go to: https://github.com/Samazat/tolstoy-daily-wisdom/settings/secrets/actions

Click "New repository secret" for each one:

### 1. SMTP_HOST
- **Name:** `SMTP_HOST` (exactly like this, all caps)
- **Value:** `mail.serous.cloud`

### 2. SMTP_PORT
- **Name:** `SMTP_PORT` (exactly like this, all caps)
- **Value:** `2525`

### 3. SMTP_USER
- **Name:** `SMTP_USER` (exactly like this, all caps)
- **Value:** `github` (or whatever username you set in Docker)

### 4. SMTP_PASS
- **Name:** `SMTP_PASS` (exactly like this, all caps)
- **Value:** (your SMTP password from Docker environment variables)

### 5. EMAIL_TO
- **Name:** `EMAIL_TO` (exactly like this, all caps)
- **Value:** `azat@gmx.net`

## Verification

After adding all secrets, you should see 5 secrets listed on the secrets page.

## Common Mistakes

❌ Wrong: `smtp_host` (lowercase)  
✅ Correct: `SMTP_HOST` (uppercase)

❌ Wrong: `SMTP-HOST` (with dash)  
✅ Correct: `SMTP_HOST` (with underscore)

❌ Wrong: `SMTP_HOST_` (with trailing underscore)  
✅ Correct: `SMTP_HOST` (no trailing underscore)

## Test

After adding all secrets, go to Actions tab and click "Run workflow" to test.

