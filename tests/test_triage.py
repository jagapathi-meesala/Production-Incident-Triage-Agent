import pytest
from core.triage import summarize_incident, prioritize_actions

def test_empty_description_rejected():
    with pytest.raises(ValueError):
        summarize_incident(" ")

def test_missing_context_reported():
    result = summarize_incident("API errors increased")
    assert "impact details" in result["unknowns"]
    assert result["root_cause_status"].startswith("not established")

def test_supplied_impact_preserved():
    result = summarize_incident("Latency", impact="Checkout requests slow")
    assert result["known_impact"] == "Checkout requests slow"

def test_timeline_preserved():
    result = summarize_incident("Errors", timeline="10:05 alert")
    assert result["timeline"] == "10:05 alert"

def test_evidence_preserved():
    result = summarize_incident("Errors", evidence="HTTP 500 increased")
    assert result["evidence"] == "HTTP 500 increased"

def test_priority_sorting():
    actions = [{"action":"inspect metrics","priority":"high"},
               {"action":"review alert","priority":"critical"}]
    assert prioritize_actions(actions)[0]["action"] == "review alert"

def test_reversible_preferred_on_tie():
    actions = [{"action":"restart all","priority":"high","reversible":False},
               {"action":"inspect logs","priority":"high","reversible":True}]
    assert prioritize_actions(actions)[0]["action"] == "inspect logs"

def test_invalid_actions_ignored():
    assert prioritize_actions([None, {}, {"priority":"high"}]) == []
