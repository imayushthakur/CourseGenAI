# ai_course_generator/data/data_processor.py
import os
import re
import logging
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

class DataProcessor:
    """Class for processing syllabus data and cleaning text inputs."""
    
    def __init__(self):
        self.topic_pattern = re.compile(r"^[A-Z][a-zA-Z ]+$")
        self.subtopic_pattern = re.compile(r"^-\s+([\w\s-]+)$")
    
    def parse_syllabus(self, syllabus_text: str) -> Dict[str, List[str]]:
        """Parse raw syllabus text into structured format.
        
        Args:
            syllabus_text: Raw text containing course structure
            
        Returns:
            Dictionary mapping topics to lists of subtopics
        """
        syllabus_dict = {}
        current_topic = None
        
        for line in syllabus_text.split('\n'):
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
                
            # Detect topic headers
            if self._is_topic_header(line):
                current_topic = line
                syllabus_dict[current_topic] = []
            # Detect subtopics under current topic
            elif current_topic is not None:
                subtopic_match = self.subtopic_pattern.match(line)
                if subtopic_match:
                    syllabus_dict[current_topic].append(subtopic_match.group(1))
                else:
                    logger.warning(f"Unrecognized line format: {line}")
        
        return syllabus_dict
    
    def _is_topic_header(self, line: str) -> bool:
        """Determine if a line represents a topic header."""
        return (
            len(line) > 3 and 
            not line.startswith('-') and 
            not line[0].isdigit() and 
            not line[0].islower()
        )
    
    def clean_transcript(self, transcript: str) -> str:
        """Clean and preprocess video transcript text."""
        # Remove timestamps
        transcript = re.sub(r"\[\d+:\d+\]", "", transcript)
        
        # Remove speaker annotations
        transcript = re.sub(r"\b[A-Z]+\b:", "", transcript)
        
        # Remove extra whitespace
        transcript = re.sub(r"\s+", " ", transcript).strip()
        
        # Remove special characters except basic punctuation
        transcript = re.sub(r"[^a-zA-Z0-9\s.,!?']", "", transcript)
        
        return transcript
    
    def validate_syllabus_structure(self, syllabus_dict: Dict[str, List[str]]) -> bool:
        """Validate the parsed syllabus structure."""
        if not syllabus_dict:
            return False
            
        for topic, subtopics in syllabus_dict.items():
            if not isinstance(topic, str) or not topic:
                return False
            if not isinstance(subtopics, list):
                return False
            if not all(isinstance(st, str) for st in subtopics):
                return False
                
        return True
