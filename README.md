# Production Incident Triage Agent

An offline assistant for organizing incident evidence and producing structured triage recommendations. It does not connect to monitoring, cloud, production, or ticketing systems.

## Features
- Summarize incident symptoms and timeline from supplied notes.
- Organize impact, evidence, hypotheses, and unknowns.
- Prioritize low-risk investigation and mitigation options.
- Draft concise internal incident updates and post-incident follow-ups.

## Quick start
Requires Python 3.10+.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python3 verification/readiness_audit.py
```

## Recommended input
Provide start time, affected services, user-visible symptoms, error rates, recent changes, relevant logs/metrics, scope, and actions already attempted. Redact secrets, tokens, personal data, and customer identifiers.

## Safety
Follow your organization's incident command and escalation policies. Avoid destructive commands, unreviewed database changes, or broad restarts. Preserve logs and evidence. Use approved runbooks and require an authorized human to approve mitigation steps.
