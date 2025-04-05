import os
import json
import logging
from typing import List, Dict, Any, Optional
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

from ..config import RAW_DATA_DIR

logger = logging.getLogger(__name__)

class TranscriptCollector:
    """Class to collect transcripts from videos across the web."""
    
    def __init__(self, save_dir: str = RAW_DATA_DIR):
        self.save_dir = save_dir
        os.makedirs(self.save_dir, exist_ok=True)
    
    def get_youtube_transcript(self, video_id: str) -> Optional[str]:
        """Retrieve transcript from a YouTube video."""
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            formatter = TextFormatter()
            transcript_text = formatter.format_transcript(transcript_list)
            
            # Save transcript
            video_data = {
                "video_id": video_id,
                "source": "youtube",
                "transcript": transcript_text
            }
            
            output_file = os.path.join(self.save_dir, f"youtube_{video_id}.json")
            with open(output_file, 'w') as f:
                json.dump(video_data, f, indent=2)
            
            return transcript_text
            
        except Exception as e:
            logger.error(f"Failed to retrieve transcript: {str(e)}")
            return None
    
    def extract_video_id_from_url(self, url: str) -> Optional[str]:
        """Extract YouTube video ID from URL."""
        if "youtube.com/watch?v=" in url:
            return url.split("watch?v=")[1].split("&")[0]
        elif "youtu.be/" in url:
            return url.split("youtu.be/")[1].split("?")[0]
        else:
            return None
