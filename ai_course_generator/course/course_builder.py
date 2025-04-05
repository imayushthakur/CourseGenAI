import os
import json
import logging
from typing import List, Dict, Any, Optional
import pandas as pd

from ..config import PROCESSED_DATA_DIR
from ..data.data_processor import DataProcessor
from ..models.classifier import ZeroShotClassifier
from .video_matcher import VideoMatcher

logger = logging.getLogger(__name__)

class CourseBuilder:
    """Class for building course structure with matched videos."""
    
    def __init__(self, 
                 data_processor: DataProcessor,
                 classifier: ZeroShotClassifier,
                 video_matcher: VideoMatcher,
                 output_dir: str = PROCESSED_DATA_DIR):
        self.data_processor = data_processor
        self.classifier = classifier
        self.video_matcher = video_matcher
        self.output_dir = output_dir
    
    def build_course(self, 
                    course_name: str,
                    syllabus_text: str,
                    video_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Build a course with videos matched to syllabus topics."""
        # Parse syllabus into topics and subtopics
        syllabus_dict = self.data_processor.parse_syllabus(syllabus_text)
        
        # Create a flat list of all subtopics
        all_subtopics = []
        for topic, subtopics in syllabus_dict.items():
            all_subtopics.extend(subtopics)
        
        # Extract transcripts from video data
        video_transcripts = [video.get("transcript", "") for video in video_data]
        
        # Classify all transcripts against all subtopics
        classification_results = []
        for transcript in video_transcripts:
            scores = self.classifier.classify(transcript, all_subtopics, multi_label=True)
            classification_results.append(scores)
        
        # Match videos to subtopics
        topic_video_matches = self.video_matcher.match_videos_to_topics(
            video_data, all_subtopics, classification_results
        )
        
        # Get the best video for each subtopic
        best_matches = self.video_matcher.get_best_video_for_topics(topic_video_matches)
        
        # Create the course structure
        course = {
            "name": course_name,
            "topics": []
        }
        
        for topic, subtopics in syllabus_dict.items():
            subtopics_with_videos = []
            for subtopic in subtopics:
                video_match = best_matches.get(subtopic)
                subtopics_with_videos.append({
                    "title": subtopic,
                    "video": video_match
                })
            
            course["topics"].append({
                "title": topic,
                "subtopics": subtopics_with_videos
            })
        
        # Save the course structure
        self._save_course(course, course_name)
        
        return course
