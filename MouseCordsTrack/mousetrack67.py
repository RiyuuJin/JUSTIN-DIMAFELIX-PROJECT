from pynput import mouse
import random

def on_move(x, y):
    if "67" in str(x) or "67" in str(y):
        jokes = [
            "67 LOL ",
            "SIX SEVENN",
            "67 MOMENT",
            "BRO FOUND THE 67 COORDINATES",
            "67 BRAINROT ACTIVATED ",
            "WHAT THE 67",
            "SIX SEVENNNNN ",
            "THE 67 IS EVERYWHERE"
        ]

        print(random.choice(jokes) * 5)

with mouse.Listener(on_move=on_move) as listener:
    listener.join()
