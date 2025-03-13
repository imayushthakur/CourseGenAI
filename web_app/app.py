import streamlit as st
from models.transcript_scraper import extract_transcript
from models.zero_shot_classifier import classify_video_transcript
from utils.text_processing import clean_text
from utils.syllabus_manager import get_subtopics

st.title("AI-Powered Course Creation System 📚🤖")
st.write("Enter video URL and select a course to classify the content!")

video_url = st.text_input("Enter YouTube Video URL:")
course_name = st.selectbox("Select Course", ["Machine Learning", "Data Science", "Deep Learning"])

if st.button("Classify Video Content"):
    transcript = extract_transcript(video_url)
    cleaned_transcript = clean_text(transcript)
    sub_topics = get_subtopics(course_name)

    if not sub_topics:
        st.error("Invalid Course Name")
    else:
        best_match, confidence = classify_video_transcript(cleaned_transcript, sub_topics)
        st.subheader("Classification Result")
        st.write(f"**Assigned Sub-topic:** {best_match} (Confidence: {confidence:.2f})")
