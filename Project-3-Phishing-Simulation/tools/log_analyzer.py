"""Log Analyzer - analyzes simulation logs"""

import json, os
from collections import defaultdict
from datetime import datetime


def analyze():
    log_path = os.path.join(os.path.dirname(__file__), '..', 'reports', 'logs', 'simulation_log.json')
    log_path = os.path.abspath(log_path)

    if not os.path.exists(log_path):
        print("\n  No simulation data yet. Run the server first!\n")
        return

    with open(log_path) as f:
        logs = json.load(f)

    print('=' * 60)
    print('  SIMULATION ANALYSIS REPORT')
    print('=' * 60)
    print(f'  Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print(f'  Total Interactions: {len(logs)}')

    actions = defaultdict(int)
    scenarios = defaultdict(int)
    creds = 0

    for e in logs:
        actions[e.get('action', '?')] += 1
        scenarios[e.get('scenario', '?')] += 1
        if e.get('action') == 'credential_submit':
            creds += 1

    print('-' * 60)
    for a, c in actions.items():
        print(f'  {a}: {c}')
    print('-' * 60)
    for s, c in scenarios.items():
        print(f'  {s}: {c} interactions')
    print('-' * 60)
    print(f'  Credentials Captured: {creds}')

    if creds > 0:
        rate = creds / max(actions.get('page_visit', 1), 1) * 100
        print(f'  Phishing Success Rate: {rate:.1f}%')
    print('=' * 60)


if __name__ == '__main__':
    analyze()
