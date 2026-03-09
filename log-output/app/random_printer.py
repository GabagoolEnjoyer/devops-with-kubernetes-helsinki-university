import time
import string
import random
from datetime import datetime


def generate_random_string(length: int = 16) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))


def main():
    # Генерируем и храним строку в памяти
    random_string = generate_random_string()

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {random_string}")
        time.sleep(5)


if __name__ == "__main__":
    main()
