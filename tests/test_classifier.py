from models.zero_shot_classifier import classify_video_transcript

def test_classify_video_transcript():
    sample_transcript = "Neural networks are a key part of deep learning models."
    sub_topics = ["Supervised Learning", "Neural Networks", "Feature Engineering"]
    best_match, confidence = classify_video_transcript(sample_transcript, sub_topics)

    assert isinstance(best_match, str)
    assert 0 <= confidence <= 1
