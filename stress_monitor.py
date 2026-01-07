def check_stress(mood_history):
    stressed_count = mood_history.count("stressed")
    if stressed_count >= 3:
        return True
    return False
