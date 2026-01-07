def recommend_task(mood):
    task_map = {
        "happy": "Creative Brainstorming Task",
        "stressed": "Light Admin + Meditation",
        "angry": "Independent Technical Task",
        "sad": "Learning / Training Task",
        "neutral": "Routine Office Work"
    }
    return task_map.get(mood, "General Task")
