# 📖 Мысли мудрыхъ людей на каждый день

**Daily wisdom from Tolstoy's 1903 collection, delivered via email via SMTP.**

## The Concept

1. GitHub Action runs daily at 6 AM UTC
2. It retrieves today's wisdom (Julian calendar corrected)
3. Sends a beautifully formatted email via your SMTP server
4. You receive the wisdom directly in your inbox

## Setup

1. Fork this repository
2. Configure GitHub Secrets with your SMTP credentials:
   - Go to **Settings → Secrets and variables → Actions**
   - Add the following secrets:
     - `SMTP_HOST` - Your SMTP server (e.g., `mail.serous.cloud`)
     - `SMTP_PORT` - SMTP port (e.g., `2525`)
     - `SMTP_USER` - SMTP username (e.g., `github`)
     - `SMTP_PASS` - SMTP password
     - `EMAIL_TO` - Your email address to receive the wisdom
3. That's it! You'll get wisdom every morning.

### Adjusting the Time

Edit `.github/workflows/daily-wisdom.yml` and change the cron schedule:

```yaml
schedule:
  - cron: '0 6 * * *'  # 6 AM UTC
```

Use [crontab.guru](https://crontab.guru/) to find your preferred time.

## About the Calendar

The original 1903 book uses the **Julian (Old Style) calendar**, which was 13 days behind the Gregorian calendar. 

This script automatically corrects for the offset:
- Your Gregorian January 14 = Julian January 1 (first entry in the book)
- Your Gregorian January 1 = Julian December 19

So you get the wisdom Tolstoy intended for that actual day of the year.

## About the Book

«Мысли мудрыхъ людей на каждый день» (Thoughts of Wise People for Every Day) was compiled by Leo Tolstoy in 1903 during a severe illness. It contains 366 daily entries with wisdom from:

- Epictetus
- Marcus Aurelius  
- Buddha
- Confucius
- Lao Tzu
- Pascal
- Ruskin
- Seneca
- The Talmud
- The Gospels
- And many others

Tolstoy wrote:

> «Я по себѣ знаю, какую это придаётъ силу, спокойствіе и счастье — входить въ общеніе съ такими душами какъ Сократъ, Эпиктетъ...»
>
> "I know from myself what strength, peace and happiness it gives to commune with such souls as Socrates, Epictetus..."

## SMTP Configuration

The workflow uses your SMTP server to send emails. Make sure your SMTP server:
- Supports authentication (username/password)
- Uses STARTTLS (default) or SSL/TLS
- Is accessible from GitHub Actions runners

If your SMTP server uses SSL/TLS instead of STARTTLS, you can add an optional secret:
- `SMTP_USE_TLS` - Set to `false` to use SSL/TLS instead of STARTTLS

## Contributing

All 366 entries have been transcribed from the 1903 edition. The collection is complete!

## License

The original text is in the public domain. This code is MIT licensed.

---

*"Дѣлай то, что должно, и будь что будетъ."*
