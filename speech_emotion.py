import librosa
import numpy as np
import os


def extract_features(audio_path):
    """
    Extract MFCC features from an audio file
    """
    try:
        # Load audio file
        y, sr = librosa.load(audio_path, duration=3, offset=0.5)

        # Extract MFCC features
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)

        # Take mean of MFCCs
        mfccs_mean = np.mean(mfccs.T, axis=0)

        return mfccs_mean

    except Exception as e:
        print("Error extracting features:", e)
        return None


def detect_speech_emotion(audio_path):
    """
    Dummy emotion detection (rule-based)
    Replace with ML model later
    """
    if not os.path.exists(audio_path):
        return "Audio file not found"

    features = extract_features(audio_path)

    if features is None:
        return "Could not process audio"

    # Simple rule-based emotion logic (for demo)
    energy = np.mean(features)

    if energy > 20:
        return "Happy"
    elif energy > 10:
        return "Neutral"
    else:
        return "Sad"
