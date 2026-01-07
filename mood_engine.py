def infer_final_mood(text_mood, face_mood, speech_mood):
    moods = [text_mood, face_mood, speech_mood]
    return max(set(moods), key=moods.count)
