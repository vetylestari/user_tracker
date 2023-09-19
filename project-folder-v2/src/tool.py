import hashlib

def hash(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()