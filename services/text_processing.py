def clean_notes(raw_text: str) -> str:
    return raw_text.replace('\n', ' ').strip()