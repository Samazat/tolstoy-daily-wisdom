# Setup Guide - GitHub Secrets

## Step 1: Add GitHub Secrets

1. Go to your repository: https://github.com/Samazat/tolstoy-daily-wisdom
2. Click on **"Settings"** (top menu bar, right side)
3. In the left sidebar, click **"Secrets and variables"** → **"Actions"**
4. Click the **"New repository secret"** button (green button, top right)

Add these 5 secrets one by one:

### Secret 1: SMTP_HOST
- **Name:** `SMTP_HOST`
- **Value:** `mail.serous.cloud`
- Click **"Add secret"**

### Secret 2: SMTP_PORT
- **Name:** `SMTP_PORT`
- **Value:** `2525`
- Click **"Add secret"**

### Secret 3: SMTP_USER
- **Name:** `SMTP_USER`
- **Value:** `github` (or whatever username you set in your Docker container)
- Click **"Add secret"**

### Secret 4: SMTP_PASS
- **Name:** `SMTP_PASS`
- **Value:** Your SMTP password (the one you set in Docker environment variables)
- Click **"Add secret"**

### Secret 5: EMAIL_TO
- **Name:** `EMAIL_TO`
- **Value:** `azat@gmx.net`
- Click **"Add secret"**

## Step 2: Test the Workflow

### Option A: Using the GitHub UI (Easiest)

1. Go to the **"Actions"** tab (top menu bar)
2. You should see **"Daily Wisdom"** workflow in the list
3. Click on **"Daily Wisdom"**
4. On the right side, you'll see a button **"Run workflow"** (dropdown)
5. Click **"Run workflow"** → **"Run workflow"** (green button)
6. The workflow will start running
7. Click on the running workflow to see the logs
8. Check your email at azat@gmx.net!

### Option B: Using the API (Already done)

The workflow has been triggered via API. Check:
- https://github.com/Samazat/tolstoy-daily-wisdom/actions

## Step 3: Verify Email Delivery

After the workflow completes successfully:
- Check your inbox at azat@gmx.net
- Check spam folder if you don't see it
- The email subject will be: "Daily Wisdom - [date]"

## Troubleshooting

If the workflow fails:
1. Click on the failed workflow run
2. Click on the job "send_wisdom"
3. Expand the step "Send daily wisdom via email"
4. Check the error message

Common issues:
- **"SMTP_PASS environment variable is required"** → You forgot to add the SMTP_PASS secret
- **"EMAIL_TO environment variable is required"** → You forgot to add the EMAIL_TO secret
- **Connection errors** → Check your SMTP server is accessible and credentials are correct

