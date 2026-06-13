"""PDF Report Generator"""

from fpdf import FPDF
import os, datetime


class Report(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'B', 9)
            self.set_text_color(100, 100, 100)
            self.cell(0, 6, 'CODEVEDX - Project 3: Phishing Simulation', 0, 1, 'C')
            self.set_draw_color(231, 76, 60)
            self.line(10, 12, 200, 12)
            self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def section(self, t):
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(44, 62, 80)
        self.cell(0, 12, t, 0, 1)
        self.set_draw_color(52, 152, 219)
        self.line(10, self.get_y(), 80, self.get_y())
        self.ln(6)

    def sub(self, t):
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(52, 73, 94)
        self.cell(0, 10, t, 0, 1)
        self.ln(1)

    def para(self, t):
        self.set_font('Helvetica', '', 11)
        self.set_text_color(60, 60, 60)
        self.set_x(10)
        self.multi_cell(190, 6, t)
        self.ln(3)

    def bold(self, t):
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(44, 62, 80)
        self.cell(0, 7, t, 0, 1)

    def bullet(self, t):
        self.set_font('Helvetica', '', 11)
        self.set_text_color(60, 60, 60)
        self.set_x(10)
        self.multi_cell(190, 6, '   - ' + t)

    def th(self, c1, c2):
        self.set_font('Helvetica', 'B', 10)
        self.set_fill_color(52, 152, 219)
        self.set_text_color(255, 255, 255)
        self.cell(55, 7, c1, 1, 0, fill=True)
        self.cell(135, 7, c2, 1, 1, fill=True)

    def td(self, c1, c2):
        self.set_font('Helvetica', '', 10)
        self.set_fill_color(240, 248, 255)
        self.set_text_color(60, 60, 60)
        self.cell(55, 7, c1, 1, 0, fill=True)
        self.cell(135, 7, c2, 1, 1, fill=True)


def gen():
    pdf = Report()
    pdf.set_auto_page_break(auto=True, margin=20)

    # COVER
    pdf.add_page()
    pdf.ln(35)
    pdf.set_font('Helvetica', 'B', 30)
    pdf.set_text_color(231, 76, 60)
    pdf.cell(0, 15, 'Phishing Attack Simulation', 0, 1, 'C')
    pdf.cell(0, 15, '& Awareness', 0, 1, 'C')
    pdf.ln(5)
    pdf.set_font('Helvetica', '', 14)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, 'Project 3 - Cyber Security & Ethical Hacking', 0, 1, 'C')
    pdf.ln(5)
    pdf.set_draw_color(52, 152, 219)
    pdf.line(60, pdf.get_y(), 150, pdf.get_y())
    pdf.ln(15)
    pdf.set_font('Helvetica', 'B', 13)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 8, 'CODEVEDX Internship Program', 0, 1, 'C')
    pdf.ln(20)

    for label, val in [
        ('Project Title:', 'Phishing Attack Simulation & Awareness'),
        ('Organization:', 'CODEVEDX'),
        ('Date:', datetime.datetime.now().strftime('%B %d, %Y')),
        ('Purpose:', 'Educational - Awareness Training'),
    ]:
        pdf.set_font('Helvetica', 'B', 11)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(55, 8, label, 0, 0, 'R')
        pdf.set_font('Helvetica', '', 11)
        pdf.cell(0, 8, '  ' + val, 0, 1)

    # SECTIONS
    pdf.add_page()
    pdf.section('1. Introduction')
    pdf.para('Phishing is one of the most prevalent cyberattack vectors. 91% of all cyberattacks begin with a phishing email. This project simulates phishing attacks in a controlled educational environment to demonstrate how they work and how to prevent them.')
    pdf.sub('Objectives')
    for o in [
        'Understand phishing attack mechanics',
        'Create realistic simulation pages',
        'Develop phishing detection tools',
        'Build interactive awareness training',
        'Generate analytical reports',
    ]:
        pdf.bullet(o)

    pdf.add_page()
    pdf.section('2. Phishing Overview')
    pdf.sub('Types of Phishing')
    for name, desc in [
        ('Email Phishing', 'Mass emails impersonating companies.'),
        ('Spear Phishing', 'Targeted attacks using personal info.'),
        ('Whaling', 'Targeting executives.'),
        ('Clone Phishing', 'Copies of legitimate emails.'),
        ('Smishing', 'Phishing via SMS.'),
        ('Vishing', 'Phishing via phone calls.'),
    ]:
        pdf.bold(name)
        pdf.para(desc)
    pdf.sub('Statistics')
    for s in ['91% of attacks start with phishing', '3.4B phishing emails daily', 'Average breach cost: $4.76M']:
        pdf.bullet(s)

    pdf.add_page()
    pdf.section('3. Project Architecture')
    pdf.th('Technology', 'Purpose')
    for t, p in [('Python 3', 'Core language'), ('Flask', 'Web framework'), ('HTML/CSS', 'Templates'), ('JSON', 'Data storage')]:
        pdf.td(t, p)

    pdf.add_page()
    pdf.section('4. Implementation')
    pdf.para('The project uses a Flask web server hosting 3 phishing scenarios. Each scenario captures user interactions and displays immediate awareness warnings. Passwords are masked for safety.')
    pdf.bold('Key Features:')
    for f in ['3 phishing scenarios', 'Real-time logging', 'Instant awareness warnings', 'JSON API reports', 'Password masking']:
        pdf.bullet(f)

    pdf.add_page()
    pdf.section('5. Simulation Scenarios')
    pdf.sub('Scenario 1: Fake Google Login')
    pdf.th('Attribute', 'Value')
    pdf.td('Attack Type', 'Credential Harvesting')
    pdf.td('Risk Level', 'HIGH')
    pdf.ln(2)
    for rf in ['URL is not accounts.google.com', 'Hosted on different domain', 'No Google OAuth']:
        pdf.bullet(rf)

    pdf.sub('Scenario 2: Fake Banking Portal')
    pdf.th('Attribute', 'Value')
    pdf.td('Attack Type', 'Credential Harvesting')
    pdf.td('Risk Level', 'CRITICAL')
    pdf.ln(2)
    for rf in ['False urgency alert', 'Fake bank name', 'Fake SSL badges']:
        pdf.bullet(rf)

    pdf.sub('Scenario 3: Email Account Update Scam')
    pdf.th('Attribute', 'Value')
    pdf.td('Attack Type', 'Urgency Scam')
    pdf.td('Risk Level', 'HIGH')
    pdf.ln(2)
    for rf in ['Generic "Dear Customer" greeting', '24-hour suspension threat', 'Password request via email']:
        pdf.bullet(rf)

    pdf.add_page()
    pdf.section('6. Detection Tools')
    pdf.sub('URL Checker')
    pdf.para('Analyzes URLs for 9 phishing indicators including HTTPS, typosquatting, suspicious TLDs, and phishing keywords.')
    pdf.sub('Email Analyzer')
    pdf.para('Analyzes email content across 7 categories: urgency, threats, greed, credential requests, impersonation, suspicious links, and grammar.')

    pdf.add_page()
    pdf.section('7. Awareness Training')
    pdf.para('4 interactive modules with quizzes covering phishing identification, types, and protection strategies.')

    pdf.add_page()
    pdf.section('8. Results & Analysis')
    pdf.para('The simulation tracks page visits, credential submissions, awareness warnings viewed, and unique IPs. All data is logged to JSON for analysis.')

    pdf.add_page()
    pdf.section('9. Recommendations')
    pdf.sub('For Individuals')
    for r in ['Enable 2FA on all accounts', 'Use a password manager', 'Verify URLs', 'Never click suspicious links', 'Be suspicious of urgency']:
        pdf.bullet(r)
    pdf.sub('For Organizations')
    for r in ['Quarterly phishing training', 'Implement SPF/DKIM/DMARC', 'Deploy email filtering', 'Maintain incident response plan']:
        pdf.bullet(r)

    pdf.add_page()
    pdf.section('10. Conclusion')
    pdf.para('This project demonstrates phishing attack mechanisms through realistic simulations and provides tools for detection and awareness training. The key takeaway is that phishing prevention requires technical controls, human awareness, and organizational policies working together.')

    pdf.add_page()
    pdf.section('11. References')
    for i, ref in enumerate([
        'OWASP - Phishing Guide', 'NIST Cybersecurity Framework',
        'SANS Phishing Training', 'APWG Phishing Trends Report',
        'Verizon DBIR Report', 'CISA Phishing Guidance',
        'Microsoft Security Report', 'Google Safe Browsing',
        'Flask Documentation', 'Python Documentation',
    ], 1):
        pdf.set_font('Helvetica', '', 11)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(0, 8, f'[{i}] {ref}', 0, 1)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'reports')
    out = os.path.abspath(out)
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, 'Phishing_Simulation_Report.pdf')
    pdf.output(path)
    print(f"\nPDF Report saved: {path}")
    print(f"Pages: {pdf.page_no()}\n")


if __name__ == '__main__':
    gen()
