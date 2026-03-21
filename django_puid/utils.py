import secrets
import time


def base36_encode(number: int) -> str:
    if number == 0:
        return "0"
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    base36 = ""
    while number:
        number, i = divmod(number, 36)
        base36 = chars[i] + base36
    return base36


def generate_id(prefix: str, entropy: int = 6, separator: str = "_") -> str:
    timestamp_b36 = base36_encode(int(time.time() * 1000))
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    random_part = "".join(secrets.choice(chars) for _ in range(entropy))
    return f"{prefix}{separator}{timestamp_b36}{random_part}"
