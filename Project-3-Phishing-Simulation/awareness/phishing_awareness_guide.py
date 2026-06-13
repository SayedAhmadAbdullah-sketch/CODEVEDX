"""Interactive Phishing Awareness Training"""

MODULES = [
    {
        'id': 1, 'title': 'What is Phishing?',
        'content': """
============================================================
  MODULE 1: What is Phishing?
============================================================

Phishing is a social engineering attack where criminals impersonate
legitimate organizations to steal sensitive information.

KEY STATISTICS:
  - 91% of cyberattacks begin with a phishing email
  - 3.4 billion phishing emails sent daily
  - Average cost of a phishing breach: $4.76 million
""",
        'quiz': {
            'q': 'What percentage of cyberattacks start with phishing?',
            'opts': ['A) 50%', 'B) 75%', 'C) 91%', 'D) 25%'],
            'a': 'C'
        }
    },
    {
        'id': 2, 'title': 'How to Identify Phishing',
        'content': """
============================================================
  MODULE 2: How to Identify Phishing
============================================================

RED FLAGS:
  1. URGENT LANGUAGE - "Act now or lose access!"
  2. GENERIC GREETINGS - "Dear Customer"
  3. SUSPICIOUS SENDER - support@amaz0n-security.com
  4. MISMATCHED LINKS - Display vs actual URL differ
  5. GRAMMAR ERRORS - Subtle spelling mistakes
  6. REQUESTS FOR PERSONAL INFO - Asking for passwords
  7. UNEXPECTED ATTACHMENTS - .exe, .zip files
""",
        'quiz': {
            'q': 'Which is a phishing indicator?',
            'opts': ['A) Your actual name', 'B) HTTPS URL', 'C) "Dear Customer" greeting', 'D) Official domain'],
            'a': 'C'
        }
    },
    {
        'id': 3, 'title': 'Types of Phishing',
        'content': """
============================================================
  MODULE 3: Types of Phishing Attacks
============================================================

  EMAIL PHISHING  - Mass emails impersonating companies
  SPEAR PHISHING  - Targeted attacks using personal info
  WHALING         - Targeting executives (CEOs, CFOs)
  CLONE PHISHING  - Copies of legitimate emails
  SMISHING        - Phishing via SMS text messages
  VISHING         - Phishing via phone calls
""",
        'quiz': {
            'q': 'What is Whaling?',
            'opts': ['A) SMS phishing', 'B) Targeting executives', 'C) Mass email phishing', 'D) Voice phishing'],
            'a': 'B'
        }
    },
    {
        'id': 4, 'title': 'How to Protect Yourself',
        'content': """
============================================================
  MODULE 4: How to Protect Yourself
============================================================

TOP 10 PROTECTION STRATEGIES:
  1. Enable Two-Factor Authentication (2FA)
  2. Use a password manager
  3. Verify URLs carefully
  4. Don't click email links - navigate directly
  5. Be suspicious of urgency
  6. Check sender addresses
  7. Keep software updated
  8. Report suspicious emails
  9. Use anti-phishing toolbars
  10. Educate yourself and others
""",
        'quiz': {
            'q': 'Most effective protection against phishing?',
            'opts': ['A) Antivirus', 'B) Two-Factor Authentication', 'C) Strong password', 'D) VPN'],
            'a': 'B'
        }
    }
]


def main():
    print("\n" + "=" * 60)
    print("  PHISHING AWARENESS TRAINING")
    print("  CODEVEDX - Cyber Security & Ethical Hacking")
    print("=" * 60)

    scores = []
    for m in MODULES:
        input(f"\n  Press Enter for Module {m['id']}: {m['title']}...")
        print(m['content'])
        quiz = m['quiz']
        print(f"  QUIZ: {quiz['q']}")
        for o in quiz['opts']:
            print(f"    {o}")
        ans = input("\n  Your answer (A/B/C/D): ").strip().upper()
        if ans == quiz['a']:
            print("  Correct!")
            scores.append(True)
        else:
            print(f"  Wrong! Answer: {quiz['a']}")
            scores.append(False)
        input("  Press Enter to continue...")

    correct = sum(scores)
    total = len(scores)
    print(f"\n{'=' * 60}")
    print(f"  TRAINING COMPLETE!")
    print(f"  Score: {correct}/{total} ({correct*100//total}%)")
    if correct == total:
        print("  Perfect! You're a phishing awareness expert!")
    print(f"{'=' * 60}\n")


if __name__ == '__main__':
    main()
