import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_transcript(video_url):
    """Extracts transcript from a given YouTube video URL."""
    video_id = re.search(r"v=([a-zA-Z0-9_-]+)", video_url).group(1)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry["text"] for entry in transcript])
        return text
    except Exception as e:
        return f"Error extracting transcript: {e}"
