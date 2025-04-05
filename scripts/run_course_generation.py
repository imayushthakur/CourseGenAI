import os
import argparse
import logging
from typing import List

from ai_course_generator.data.transcript_collector import TranscriptCollector
from ai_course_generator.data.data_processor import DataProcessor
from ai_course_generator.models.classifier import ZeroShotClassifier
from ai_course_generator.course.video_matcher import VideoMatcher
from ai_course_generator.course.course_builder import CourseBuilder
from ai_course_generator.utils.helpers import setup_logging, extract_youtube_id

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Generate an AI course from a syllabus and videos.')
    
    parser.add_argument('--course-name', '-n', type=str, required=True,
                      help='Name of the course')
    parser.add_argument('--syllabus', '-s', type=str, required=True,
                      help='Path to a text file containing the course syllabus')
    parser.add_argument('--videos', '-v', type=str, required=True,
                      help='Path to a text file containing video URLs or IDs (one per line)')
    parser.add_argument('--output-dir', '-o', type=str, default='data/processed',
                      help='Directory to save the generated course files')
    parser.add_argument('--threshold', '-t', type=float, default=0.7,
                      help='Minimum score threshold for matching videos to topics')
    
    return parser.parse_args()

def main():
    """Run the course generation process."""
    args = parse_arguments()
    setup_logging()
    
    # Read syllabus and video list
    syllabus_text = open(args.syllabus, 'r').read()
    video_urls = [line.strip() for line in open(args.videos, 'r').readlines() if line.strip()]
    
    # Initialize components
    transcript_collector = TranscriptCollector()
    data_processor = DataProcessor()
    classifier = ZeroShotClassifier()
    video_matcher = VideoMatcher(threshold=args.threshold)
    
    # Collect video transcripts
    video_data = []
    for url in video_urls:
        video_id = extract_youtube_id(url) if '://' in url else url
        if video_id:
            transcript = transcript_collector.get_youtube_transcript(video_id)
            if transcript:
                video_data.append({
                    "video_id": video_id,
                    "url": url if '://' in url else f"https://www.youtube.com/watch?v={video_id}",
                    "transcript": transcript,
                    "source": "youtube"
                })
    
    # Build the course
    course_builder = CourseBuilder(
        data_processor=data_processor,
        classifier=classifier,
        video_matcher=video_matcher,
        output_dir=args.output_dir
    )
    
    course = course_builder.build_course(
        course_name=args.course_name,
        syllabus_text=syllabus_text,
        video_data=video_data
    )
    
    print(f"Course generation complete!")

if __name__ == "__main__":
    main()
