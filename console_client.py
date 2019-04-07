from os import get_terminal_size

from game import Game
from getkey import getkey
from snake import Snake

wid, hei = get_terminal_size()

game: Game = Game(wid, hei, Snake("Snake", (0, 255, 0)))

key: str = getkey()
while key not in "\x03\x04\x1aqe":
    if key in ["\033[A", "w", "k"]:  # UP
        print("up")
    elif key in ["\033[B", "s", "j"]:  # DOWN
        print("down")
    elif key in ["\033[C", "d", "l"]:  # RIGHT
        print("right")
    elif key in ["\033[D", "a", "h"]:  # LEFT
        print("left")
    key: str = getkey()
