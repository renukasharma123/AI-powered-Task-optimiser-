def detect_text_emotion(text):
    positive_words = ["happy", "good", "great", "excellent", "joy"]
    negative_words = ["sad", "bad", "angry", "stress", "tired"]

    text = text.lower()

    if any(word in text for word in positive_words):
        return "happy"
    elif any(word in text for word in negative_words):
        return "stressed"
    else:
        return "neutral"
