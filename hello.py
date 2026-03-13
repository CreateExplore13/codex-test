from datetime import datetime


def print_time() -> None:
    """Print the current local time in HH:MM:SS format."""
    print(datetime.now().strftime("%H:%M:%S"))


print("Hello Codex")
print_time()
