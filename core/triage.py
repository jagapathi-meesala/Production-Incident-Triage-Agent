"""Pure helpers for structuring incident information."""
def summarize_incident(description: str, impact: str = "", timeline: str = "", evidence: str = "") -> dict:
    if not isinstance(description, str) or not description.strip():
        raise ValueError("description must be a non-empty string")
    return {
        "description": description.strip(),
        "known_impact": impact.strip() if isinstance(impact, str) else "",
        "timeline": timeline.strip() if isinstance(timeline, str) else "",
        "evidence": evidence.strip() if isinstance(evidence, str) else "",
        "hypotheses": [],
        "unknowns": [
            label for label, value in [
                ("impact details", impact),
                ("timeline", timeline),
                ("evidence or logs", evidence),
            ] if not isinstance(value, str) or not value.strip()
        ],
        "root_cause_status": "not established from supplied information",
    }

def prioritize_actions(actions: list[dict]) -> list[dict]:
    """Sort actions by explicit priority and prefer reversible actions on ties."""
    valid = [dict(a) for a in actions if isinstance(a, dict) and a.get("action")]
    priority = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    return sorted(valid, key=lambda a: (
        priority.get(str(a.get("priority", "medium")).lower(), 2),
        not bool(a.get("reversible", True)),
    ))
