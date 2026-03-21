import secrets
import time

BASE36_CHARS = "0123456789abcdefghijklmnopqrstuvwxyz"


def base36_encode(number: int) -> str:
    if number == 0:
        return "0"
    base36 = ""
    while number:
        number, i = divmod(number, 36)
        base36 = BASE36_CHARS[i] + base36
    return base36


def generate_id(prefix: str, random_length: int = 6, separator: str = "_") -> str:
    timestamp_b36 = base36_encode(int(time.time() * 1000))
    random_part = "".join(secrets.choice(BASE36_CHARS) for _ in range(random_length))
    return f"{prefix}{separator}{timestamp_b36}{random_part}"
