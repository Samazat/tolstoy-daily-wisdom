# 📖 Мысли мудрыхъ людей на каждый день

**Daily wisdom from Tolstoy's 1903 collection, delivered via GitHub's failure notifications.**

## The Concept

1. GitHub Action runs daily at 6 AM UTC
2. It prints today's wisdom (Julian calendar corrected) to stdout
3. Then it **intentionally fails** (exit code 1)
4. GitHub emails you about the "failure"
5. The email contains the wisdom in the logs

It's a feature, not a bug.

## Setup

1. Fork this repository
2. Go to **Settings → Notifications** and ensure you receive emails for failed workflows
3. That's it. You'll get wisdom every morning.

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

## Contributing

The entries are being transcribed from the 1903 edition. Many days are still missing. 

If you'd like to help, edit `wisdom.py` and add entries in the format:

```python
(month, day): """N месяца

Текстъ мудрости...

— Источникъ""",
```

Keep the original pre-revolutionary orthography (ъ, ѣ, i, ѳ) where possible.

## License

The original text is in the public domain. This code is MIT licensed.

---

*"Дѣлай то, что должно, и будь что будетъ."*
