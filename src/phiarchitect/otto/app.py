"""
run the main app
"""
from .otto import Otto


def run() -> None:
    reply = Otto().run()
    print(reply)
