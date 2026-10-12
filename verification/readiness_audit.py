from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    "agent.yaml", "SOUL.md", "README.md", "RULES.md", "DUTIES.md", "AGENTS.md",
    "EXPLAINABILITY.md", "requirements.txt", "pytest.ini", "core/triage.py",
    "tools/summarize-incident.yaml", "tools/prioritize-triage-actions.yaml",
    "tools/draft-incident-update.yaml", "skills/incident-assessment/SKILL.md",
    "skills/evidence-correlation/SKILL.md", "skills/mitigation-planning/SKILL.md",
    "tests/test_triage.py", "verification/readiness_audit.py"
]
missing = [p for p in required if not (root / p).is_file()]
if missing:
    print("FAIL: missing required files:", ", ".join(missing))
    sys.exit(1)
print(f"PASS: all {len(required)}/{len(required)} required files present")
