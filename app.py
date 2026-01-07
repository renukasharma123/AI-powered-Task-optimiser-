import streamlit as st

from text_emotion import detect_text_emotion
from face_emotion import detect_face_emotion
from speech_emotion import detect_speech_emotion
from mood_engine import infer_final_mood
from task_recommender import recommend_task
from stress_monitor import check_stress

st.set_page_config(page_title="AI Powered Task Optimizer")

st.title("🧠 AI Powered Task Optimizer")

mood_history = []

text = st.text_area("Enter your thoughts")

if st.button("Analyze Emotion & Recommend Task"):
    text_mood = detect_text_emotion(text)
    face_mood = detect_face_emotion()
    speech_mood = detect_speech_emotion("sample.wav")  # demo audio

    final_mood = infer_final_mood(text_mood, face_mood, speech_mood)
    mood_history.append(final_mood)

    st.subheader(f"Detected Mood: {final_mood}")
    st.success(f"Recommended Task: {recommend_task(final_mood)}")

    if check_stress(mood_history):
        st.error("⚠ Stress Alert! HR Notification Triggered")
