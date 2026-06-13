"""
URL Phishing Detection Tool
Usage: python3 url_checker.py <url>
"""

import re, sys, socket, urllib.parse
from datetime import datetime

LEGIT_DOMAINS = [
    'google.com', 'facebook.com', 'amazon.com', 'apple.com',
    'microsoft.com', 'netflix.com', 'paypal.com', 'ebay.com',
    'twitter.com', 'instagram.com', 'linkedin.com', 'yahoo.com'
]
SUSPICIOUS_TLDS = ['.tk', '.ml', '.ga', '.cf', '.gq', '.xyz', '.top', '.click']
PHISHING_KEYWORDS = [
    'verify', 'secure', 'account', 'update', 'confirm', 'login',
    'signin', 'password', 'alert', 'suspend', 'urgent', 'validate'
]


class PhishingURLChecker:
    def __init__(self, url):
        self.url = url
        self.parsed = urllib.parse.urlparse(url)
        self.domain = self.parsed.netloc
        self.issues = []
        self.score = 0

    def check_https(self):
        if self.parsed.scheme != 'https':
            self.issues.append(('[MEDIUM]', 'No HTTPS'))
            self.score += 20

    def check_ip(self):
        try:
            socket.inet_aton(self.domain.split(':')[0])
            self.issues.append(('[HIGH]', 'Domain is an IP address'))
            self.score += 40
        except socket.error:
            pass

    def check_domain_length(self):
        if len(self.domain) > 30:
            self.issues.append(('[MEDIUM]', f'Long domain ({len(self.domain)} chars)'))
            self.score += 15

    def check_tld(self):
        for tld in SUSPICIOUS_TLDS:
            if self.domain.endswith(tld):
                self.issues.append(('[HIGH]', f'Suspicious TLD: {tld}'))
                self.score += 30
                break

    def check_typosquatting(self):
        for legit in LEGIT_DOMAINS:
            cleaned = self.domain.replace('www.', '')
            if legit in cleaned and cleaned != legit:
                self.issues.append(('[HIGH]', f'Typosquatting of {legit}'))
                self.score += 35
                break

    def check_subdomains(self):
        if len(self.domain.split('.')) > 3:
            self.issues.append(('[MEDIUM]', 'Excessive subdomains'))
            self.score += 15

    def check_keywords(self):
        found = [kw for kw in PHISHING_KEYWORDS if kw in self.url.lower()]
        if found:
            self.issues.append(('[MEDIUM]', f'Phishing keywords: {", ".join(found)}'))
            self.score += len(found) * 5

    def check_chars(self):
        if '@' in self.url:
            self.issues.append(('[HIGH]', '@ symbol hides real URL'))
            self.score += 30

    def check_homograph(self):
        nums = re.findall(r'[0-9]', self.domain.replace('www.', '').split('.')[0])
        if len(nums) >= 2:
            self.issues.append(('[MEDIUM]', 'Possible homograph attack'))
            self.score += 20

    def analyze(self):
        print('=' * 60)
        print('  URL PHISHING ANALYSIS')
        print('=' * 60)
        print(f'  URL: {self.url}')
        print(f'  Domain: {self.domain}')
        print(f'  Scheme: {self.parsed.scheme}')
        print('-' * 60)

        for check in [self.check_https, self.check_ip, self.check_domain_length,
                       self.check_tld, self.check_typosquatting, self.check_subdomains,
                       self.check_keywords, self.check_chars, self.check_homograph]:
            try:
                check()
            except Exception as e:
                self.issues.append(('[ERROR]', str(e)))

        if self.issues:
            for sev, desc in self.issues:
                print(f'  {sev} {desc}')
        else:
            print('  No phishing indicators found.')

        print('-' * 60)
        print(f'  Risk Score: {self.score}/100')
        if self.score >= 50:
            print('  HIGH RISK - Likely phishing!')
        elif self.score >= 25:
            print('  MEDIUM RISK - Suspicious')
        else:
            print('  LOW RISK - Appears safe')
        print(f'  Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        print('=' * 60)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 url_checker.py <url>')
        sys.exit(1)
    PhishingURLChecker(sys.argv[1]).analyze()
