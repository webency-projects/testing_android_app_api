import hashlib


def generate_hash_token(*args: str) -> str:
    return hashlib.sha512("".join(args).encode()).hexdigest()



