def claim_summary_template(claim_data, notes):
    return f"""
You are a professional insurance report generator.

Given the following claim data and adjuster notes, generate a formal summary report:

Claim ID: {claim_data['claim_id']}
Policyholder: {claim_data['policyholder_name']}
Policy Type: {claim_data['policy_type']}
Incident Date: {claim_data['incident_date']}
Claim Amount: ${claim_data['claim_amount']}
Claim Status: {claim_data['claim_status']}
Adjuster Notes: {notes}

Format:

1. Claim Overview
2. Incident Description
3. Assessment
4. Recommendation
"""