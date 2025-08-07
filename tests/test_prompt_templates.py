from llm.prompt_templates import claim_summary_prompt

def test_claim_summary_prompt_contains_expected_sections():
    dummy_claim = {
        "claim_id": "CLM123",
        "policyholder_name": "John Doe",
        "policy_type": "Auto",
        "incident_date": "2025-01-01",
        "claim_amount": 1000,
        "claim_status": "Pending"
    }
    notes = "Minor accident."

    prompt = claim_summary_prompt(dummy_claim, notes)

    assert "Claim ID: CLM123" in prompt
    assert "Minor accident." in prompt
    assert "Recommendation" in prompt