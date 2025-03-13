import re

def clean_text(text):
    """Removes unwanted characters and normalizes text."""
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)  # Remove multiple spaces
    return text
