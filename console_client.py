from os import get_terminal_size
from typing import List

from directions import *
from game import Game
from getkey import getkey
from snake import Snake
from timer import Timer

wid, hei = get_terminal_size()
wid //= 2

snake: Snake = Snake("Snake", (0, 255, 0))
game: Game = Game(wid, hei, snake)


def draw_board():
    board: List[List[int]] = [[0 for _ in range(wid)] for _ in range(hei)]
    for x, y in game.snake.body:
        board[y][x] = 1
    x, y = game.snake.body[-1]
    board[y][x] = 2

    out: List[str] = []
    for line in board:
        out.append("\r")
        for cell in line:
            if cell == 0:
                out[-1] += "\033[38;2;0;0;0m" + "\u2588" * 2
            elif cell == 1:
                out[-1] += "\033[38;2;0;127;0m" + "\u2588" * 2
            elif cell == 2:
                out[-1] += "\033[38;2;0;255;0m" + "\u2588" * 2
    print("\033c" + "\n".join(out), end='\033[0m')


def tick():
    game.tick()
    draw_board()


timer: Timer = Timer(1, tick)
timer.start()

draw_board()
key: str = getkey()
while key not in "\x03\x04\x1aqe" and not snake.dead:
    if key in ["\033[A", "w", "k"]:  # UP
        snake.change_direction(NORTH)
    elif key in ["\033[B", "s", "j"]:  # DOWN
        snake.change_direction(SOUTH)
    elif key in ["\033[C", "d", "l"]:  # RIGHT
        snake.change_direction(EAST)
    elif key in ["\033[D", "a", "h"]:  # LEFT
        snake.change_direction(WEST)
    key: str = getkey()
timer.stop()
