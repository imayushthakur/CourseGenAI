from models.transcript_scraper import extract_transcript

def test_extract_transcript():
    sample_url = "https://www.youtube.com/watch?v=ENrzD9HAZK4"
    transcript = extract_transcript(sample_url)
    assert isinstance(transcript, str)
    assert len(transcript) > 0
