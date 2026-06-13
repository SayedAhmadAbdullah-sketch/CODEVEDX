"""
Phishing Email Analyzer
Usage: python3 email_analyzer.py --demo
"""

import re
from datetime import datetime

PATTERNS = {
    'Urgency': {
        'words': ['urgent', 'immediately', 'act now', 'right away', 'expires today', 'within 24 hours'],
        'weight': 10
    },
    'Threat': {
        'words': ['suspend', 'terminate', 'locked', 'restricted', 'disabled', 'unauthorized'],
        'weight': 10
    },
    'Greed': {
        'words': ['free', 'winner', 'congratulations', 'prize', 'reward', 'cash', 'bonus'],
        'weight': 8
    },
    'Credentials': {
        'words': ['password', 'username', 'credit card', 'bank account', 'verify your identity'],
        'weight': 15
    },
    'Impersonation': {
        'words': ['dear customer', 'dear user', 'valued customer', 'dear member'],
        'weight': 8
    },
    'Suspicious Links': {
        'words': ['click here', 'click below', 'tap here'],
        'weight': 5
    },
    'Grammar': {
        'words': ['kindly', 'we apologies', 'security reason'],
        'weight': 3
    }
}


def analyze(subject, body, sender):
    full = f"{subject} {body} {sender}".lower()
    total = 0
    findings = []

    print('=' * 60)
    print('  EMAIL PHISHING ANALYSIS')
    print('=' * 60)
    print(f'  Subject: {subject}')
    print(f'  Sender:  {sender}')
    print(f'  Date:    {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print('-' * 60)

    for category, info in PATTERNS.items():
        found = [w for w in info['words'] if w in full]
        if found:
            score = info['weight'] * len(found)
            total += score
            findings.append((category, found, score))
            print(f'  [{category}] Score: {score}')
            for w in found:
                print(f'    - Matched: "{w}"')

    urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', full)
    if urls:
        print(f'\n  Links Found ({len(urls)}):')
        for u in urls:
            print(f'    -> {u}')

    print('-' * 60)
    print(f'  Phishing Score: {total}')
    if total >= 50:
        print('  VERY HIGH RISK - Almost certainly phishing!')
    elif total >= 30:
        print('  HIGH RISK - Strong phishing indicators')
    elif total >= 15:
        print('  MEDIUM RISK - Some suspicious elements')
    else:
        print('  LOW RISK - Appears relatively safe')
    print('=' * 60)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--demo':
        analyze(
            "Urgent: Your Account Will Be Suspended Within 24 Hours",
            "Dear Valued Customer, We have detected unauthorized access. "
            "Click here to verify your account: http://amaz0n-verify.com "
            "Please provide your password immediately.",
            "security@amaz0n-verify.com"
        )
    else:
        subject = input("Enter email subject: ")
        sender = input("Enter sender email: ")
        print("Enter email body (press Enter twice to finish):")
        lines = []
        empty = 0
        while True:
            line = input("> ")
            if line == "":
                empty += 1
                if empty >= 2:
                    break
            else:
                empty = 0
            lines.append(line)
        analyze(subject, "\n".join(lines), sender)
