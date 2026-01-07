import hashlib

def anonymize_user(user_id):
    return hashlib.sha256(user_id.encode()).hexdigest()
