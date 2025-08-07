import os
from dotenv import load_dotenv
from services.data_ingestion import fetch_claim_data
from services.text_processing import clean_notes
from llm.gemini_client import generate_claim_summary
from llm.prompt_templates import claim_summary_template
from reports.report_generator import render_html_report

load_dotenv()

def main():
    claim_id = "CLM123456"  # replace with dynamic input later
    claim_data = fetch_claim_data(claim_id)
    notes = clean_notes(claim_data["adjuster_notes"])

    prompt = claim_summary_template(claim_data, notes)
    summary = generate_claim_summary(prompt)

    report_data = {
        "claim_id": claim_data["claim_id"],
        "policyholder": claim_data["policyholder_name"],
        "policy_type": claim_data["policy_type"],
        "incident_date": claim_data["incident_date"],
        "claim_amount": claim_data["claim_amount"],
        "claim_status": claim_data["claim_status"],
        "summary": summary
    }

    html_path = render_html_report(report_data, f"{claim_id}.html")
    print(f"✅ Report generated at: {html_path}")

if __name__ == "__main__":
    main()
