"""
PROJECT 3 - Phishing Attack Simulation & Awareness
CODEVEDX - Cyber Security & Ethical Hacking Internship
Educational Use Only
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify
import json, os, datetime
from collections import defaultdict

app = Flask(__name__)

# Paths
LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'reports', 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

# Scenarios
SCENARIOS = {
    'google': {
        'name': 'Fake Google Login',
        'type': 'Credential Harvesting',
        'risk': 'HIGH',
        'desc': 'Simulates a fake Google sign-in page.'
    },
    'bank': {
        'name': 'Fake Banking Portal',
        'type': 'Credential Harvesting',
        'risk': 'CRITICAL',
        'desc': 'Simulates a fake bank login page.'
    },
    'email_update': {
        'name': 'Email Account Update Scam',
        'type': 'Urgency Scam',
        'risk': 'HIGH',
        'desc': 'Simulates an urgent email asking to verify account.'
    }
}


def get_client_info():
    return {
        'ip': request.remote_addr,
        'user_agent': request.headers.get('User-Agent', 'Unknown'),
        'time': datetime.datetime.now().isoformat(),
        'referrer': request.referrer or 'Direct'
    }


def log_interaction(scenario, action, data=None):
    log_file = os.path.join(LOG_DIR, 'simulation_log.json')
    logs = []
    if os.path.exists(log_file):
        try:
            with open(log_file, 'r') as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    logs.append({
        'scenario': scenario,
        'action': action,
        'client': get_client_info(),
        'data': data or {}
    })

    with open(log_file, 'w') as f:
        json.dump(logs, f, indent=2)


def make_report(logs):
    if not logs:
        return {'total': 0}
    r = {
        'total': len(logs),
        'scenarios': defaultdict(int),
        'actions': defaultdict(int),
        'creds': 0,
        'warnings': 0,
        'ips': set(),
        'timeline': []
    }
    for e in logs:
        s = e.get('scenario', '?')
        a = e.get('action', '?')
        r['scenarios'][s] += 1
        r['actions'][a] += 1
        r['ips'].add(e.get('client', {}).get('ip', '?'))
        if a == 'credential_submit':
            r['creds'] += 1
        if a == 'warning_shown':
            r['warnings'] += 1
        r['timeline'].append({
            'time': e.get('client', {}).get('time', ''),
            'scenario': s,
            'action': a
        })
    r['scenarios'] = dict(r['scenarios'])
    r['actions'] = dict(r['actions'])
    r['ips'] = len(r['ips'])
    return r


# ---- ROUTES ----

@app.route('/')
def index():
    return render_template('dashboard.html', scenarios=SCENARIOS)


@app.route('/simulate/<scenario>')
def simulate(scenario):
    if scenario not in SCENARIOS:
        return redirect(url_for('index'))
    log_interaction(scenario, 'page_visit')
    return render_template(f'{scenario}_phish.html', scenario=scenario)


@app.route('/simulate/<scenario>/submit', methods=['POST'])
def handle_submit(scenario):
    if scenario not in SCENARIOS:
        return redirect(url_for('index'))

    email = request.form.get('email', '')
    password = request.form.get('password', '')
    masked = '*' * len(password) if password else ''

    log_interaction(scenario, 'credential_submit', {
        'email': email,
        'password_masked': masked,
        'password_length': len(password)
    })

    return render_template('warning.html',
        scenario=scenario,
        info=SCENARIOS[scenario],
        email_entered=email,
        password_masked=masked)


@app.route('/awareness/<scenario>')
def awareness(scenario):
    if scenario not in SCENARIOS:
        return redirect(url_for('index'))
    log_interaction(scenario, 'warning_shown')
    return render_template('awareness.html',
        scenario=scenario,
        info=SCENARIOS[scenario])


@app.route('/report')
def report():
    log_file = os.path.join(LOG_DIR, 'simulation_log.json')
    logs = []
    if os.path.exists(log_file):
        try:
            with open(log_file, 'r') as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    return render_template('report.html', report=make_report(logs), logs=logs)


@app.route('/api/report')
def api_report():
    log_file = os.path.join(LOG_DIR, 'simulation_log.json')
    logs = []
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs = json.load(f)
    return jsonify(make_report(logs))


@app.route('/reset')
def reset():
    log_file = os.path.join(LOG_DIR, 'simulation_log.json')
    if os.path.exists(log_file):
        os.remove(log_file)
    return redirect(url_for('report'))


if __name__ == '__main__':
    print("=" * 55)
    print("  Phishing Simulation Server - Educational Only")
    print("  Dashboard: http://127.0.0.1:5000")
    print("=" * 55)
    app.run(debug=True, host='0.0.0.0', port=5000)
