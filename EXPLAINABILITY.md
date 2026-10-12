# Explainability

This document explains the agent's inputs, decision process, outputs, and limitations.

## Inputs
The agent accepts user-provided incident descriptions, service names, timestamps, symptoms, logs or metrics excerpts, recent deployment changes, known impact, and actions already attempted. Sensitive information should be redacted before submission.

## Decision
The agent separates observations from hypotheses and unknowns, organizes evidence into a timeline, and prioritizes investigation steps according to impact, urgency, reversibility, and information value. It does not infer a confirmed root cause from correlation alone.

## Limits
The agent has no live access to production systems, dashboards, alerting, logs, or ticketing. Its recommendations depend on the completeness and accuracy of supplied evidence. It cannot independently determine service health, incident severity, or whether a mitigation is safe in a particular environment.

## Tool: summarize-incident

### Inputs and Data Sources
Receives an incident description and optional timeline, impact, evidence, and recent changes supplied by the user.

### Decision and Reasoning
Organizes the supplied material into symptoms, known impact, timeline, evidence, hypotheses, and unknowns.

### Outputs and Evidence
Returns a structured incident summary using only the supplied information and explicitly marks missing details.

### Limits and Constraints
It cannot verify logs or determine root cause without additional evidence.

### Failure Handling
If the report lacks key information, it identifies missing fields and asks for clarification rather than inventing facts.

### Human Review
The incident lead checks the summary for accuracy before sharing or using it for decisions.

## Tool: prioritize-triage-actions

### Inputs and Data Sources
Receives incident context, known impact, available evidence, constraints, and actions already attempted.

### Decision and Reasoning
Ranks proposed investigation steps by urgency, risk, reversibility, and likely information value. Suggestions remain conditional when system-specific runbooks are unavailable.

### Outputs and Evidence
Returns a prioritized checklist with rationale, prerequisites, risks, and verification steps.

### Limits and Constraints
It does not execute commands, inspect production, or guarantee a mitigation will resolve the incident.

### Failure Handling
When impact or safety context is unclear, it favors evidence collection and escalation over disruptive changes.

### Human Review
An authorized responder validates each action against approved runbooks and obtains required approvals.

## Tool: draft-incident-update

### Inputs and Data Sources
Receives confirmed facts, known impact, current status, next steps, and audience supplied by the user.

### Decision and Reasoning
Creates a concise status update that distinguishes confirmed information from ongoing investigation and avoids unsupported promises.

### Outputs and Evidence
Returns a draft update for human review. Missing facts should remain marked as unknown or omitted.

### Limits and Constraints
It does not send messages, page responders, or confirm recovery.

### Failure Handling
If status or impact is uncertain, the draft states that the team is investigating and names the evidence still needed.

### Human Review
The incident commander or communications owner approves the update before distribution.

## Data Quality and Uncertainty
Logs and metrics may be incomplete, delayed, or misleading. The agent must preserve timestamps and context where provided and must not manufacture causal links.

## Security and Responsible Use
Redact credentials, access tokens, personal data, and sensitive customer identifiers. Follow organizational incident response and escalation policies. Do not disable security controls or erase evidence.

## Audit and Reproducibility
Retain the supplied timeline, key evidence references, decisions, mitigations, verification results, and follow-up actions according to organizational policy.
