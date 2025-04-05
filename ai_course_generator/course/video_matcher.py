from typing import List, Dict, Any, Optional
from ..config import CLASSIFICATION_THRESHOLD

class VideoMatcher:
    """Class for matching videos to course topics based on classification scores."""
    
    def __init__(self, threshold: float = CLASSIFICATION_THRESHOLD):
        self.threshold = threshold
    
    def match_videos_to_topics(self, 
                              video_data: List[Dict[str, Any]], 
                              topics: List[str],
                              classification_results: List[Dict[str, float]]) -> Dict[str, List[Dict[str, Any]]]:
        """Match videos to topics based on classification scores."""
        matches = {topic: [] for topic in topics}
        
        for i, (video, scores) in enumerate(zip(video_data, classification_results)):
            # Find the topic with the highest score for this video
            best_topic = max(scores.items(), key=lambda x: x[1])
            topic_name, score = best_topic
            
            if score >= self.threshold and topic_name in topics:
                video_info = {
                    "video_id": video.get("video_id", f"video_{i}"),
                    "source": video.get("source", "unknown"),
                    "score": score,
                    "url": video.get("url", "")
                }
                matches[topic_name].append(video_info)
        
        # Sort the videos for each topic by score in descending order
        for topic in matches:
            matches[topic] = sorted(matches[topic], key=lambda x: x["score"], reverse=True)
        
        return matches
    
    def get_best_video_for_topics(self, 
                                 topic_video_matches: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Optional[Dict[str, Any]]]:
        """Get the best video for each topic based on highest score."""
        best_matches = {}
        
        for topic, videos in topic_video_matches.items():
            if videos:
                best_matches[topic] = videos[0]  # The videos are already sorted by score
            else:
                best_matches[topic] = None
        
        return best_matches
