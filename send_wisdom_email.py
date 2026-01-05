#!/usr/bin/env python3
"""
Send daily wisdom via email using SMTP
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from wisdom import get_wisdom, get_julian_date

def send_wisdom_email():
    """Send today's wisdom via email."""
    
    # Get SMTP configuration from environment variables (GitHub Secrets)
    smtp_host = os.getenv('SMTP_HOST', 'mail.serous.cloud')
    smtp_port = int(os.getenv('SMTP_PORT', '2525'))
    smtp_user = os.getenv('SMTP_USER', 'github')
    smtp_pass = os.getenv('SMTP_PASS', '')
    email_to = os.getenv('EMAIL_TO', '')
    
    if not smtp_pass:
        raise ValueError("SMTP_PASS environment variable is required")
    if not email_to:
        raise ValueError("EMAIL_TO environment variable is required")
    
    # Get today's wisdom
    wisdom = get_wisdom()
    today = datetime.now()
    julian_month, julian_day = get_julian_date()
    
    # Create email
    msg = MIMEMultipart('alternative')
    msg['From'] = f"Tolstoy Wisdom <{smtp_user}@serous.cloud>"
    msg['To'] = email_to
    msg['Subject'] = f"Daily Wisdom - {today.strftime('%d.%m.%Y')} (Julian: {julian_day:02d}.{julian_month:02d})"
    
    # Create plain text version
    text_content = f"""МЫСЛИ МУДРЫХ ЛЮДЕЙ НА КАЖДЫЙ ДЕНЬ
Собраны Л. Н. Толстым (1903)

Сегодня по новому стилю: {today.strftime('%d.%m.%Y')}
По старому стилю: {julian_day:02d}.{julian_month:02d}

{'=' * 60}

{wisdom}

{'=' * 60}

«Я по себе знаю, какую это придаёт силу,
спокойствие и счастье — входить в общение
с такими душами как Сократ, Эпиктет...»
                              — Л. Н. Толстой
"""
    
    # Create HTML version
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: Georgia, serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }}
        .header {{
            text-align: center;
            border-bottom: 2px solid #8B4513;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        .date {{
            color: #666;
            font-size: 0.9em;
            margin-bottom: 20px;
        }}
        .wisdom {{
            background-color: #f9f9f9;
            padding: 20px;
            border-left: 4px solid #8B4513;
            margin: 20px 0;
            white-space: pre-wrap;
        }}
        .footer {{
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            font-style: italic;
            color: #666;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>МЫСЛИ МУДРЫХ ЛЮДЕЙ НА КАЖДЫЙ ДЕНЬ</h1>
        <p>Собраны Л. Н. Толстым (1903)</p>
    </div>
    
    <div class="date">
        Сегодня по новому стилю: <strong>{today.strftime('%d.%m.%Y')}</strong><br>
        По старому стилю: <strong>{julian_day:02d}.{julian_month:02d}</strong>
    </div>
    
    <div class="wisdom">
{wisdom}
    </div>
    
    <div class="footer">
        <p>«Я по себе знаю, какую это придаёт силу,<br>
        спокойствие и счастье — входить в общение<br>
        с такими душами как Сократ, Эпиктет...»</p>
        <p>— Л. Н. Толстой</p>
    </div>
</body>
</html>
"""
    
    # Attach both versions
    part1 = MIMEText(text_content, 'plain', 'utf-8')
    part2 = MIMEText(html_content, 'html', 'utf-8')
    
    msg.attach(part1)
    msg.attach(part2)
    
    # Send email
    try:
        print(f"Connecting to SMTP server {smtp_host}:{smtp_port}...")
        # Try STARTTLS first (common for port 2525)
        use_tls = os.getenv('SMTP_USE_TLS', 'true').lower() == 'true'
        
        if use_tls:
            server = smtplib.SMTP(smtp_host, smtp_port)
            server.starttls()  # Enable encryption
        else:
            # For SSL/TLS on port 465
            server = smtplib.SMTP_SSL(smtp_host, smtp_port)
        
        server.login(smtp_user, smtp_pass)
        print(f"Sending email to {email_to}...")
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        raise

if __name__ == "__main__":
    send_wisdom_email()

