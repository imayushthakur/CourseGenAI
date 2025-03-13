from transformers import pipeline

# Load the Zero-Shot Classification Model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_video_transcript(transcript, sub_topics):
    """Performs Zero-Shot Classification to assign transcript to a sub-topic."""
    result = classifier(transcript, sub_topics, multi_label=False)
    best_match = result["labels"][0]
    confidence = result["scores"][0]
    return best_match, confidence
