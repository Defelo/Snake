from typing import Tuple, List

from directions import *
from game import Game


class Snake:
    def __init__(self, name: str, colour: Tuple[int, int, int]):
        self.name: str = name
        self.colour: Tuple[int, int, int] = colour
        self.board: Game = None
        self.body: List[Tuple[int, int]] = None
        self.direction: int = EAST
        self.can_change_direction: bool = True
        self.dead: bool = True

    def register(self, game: Game, body: List[Tuple[int, int]]):
        self.board: Game = game
        self.body: List[Tuple[int, int]] = body
        self.dead: bool = False

    def change_direction(self, new_direction: int):
        if self.can_change_direction and (new_direction + self.direction) % 2:
            self.direction: int = new_direction
            self.can_change_direction: bool = False

    def tick(self):
        if self.dead:
            return

        headx, heady = self.body[-1]
        if self.direction == NORTH:
            heady -= 1
        elif self.direction == EAST:
            headx += 1
        elif self.direction == SOUTH:
            heady += 1
        elif self.direction == WEST:
            headx -= 1
        if not (0 <= headx < self.board.width and 0 <= heady < self.board.height):
            self.dead: bool = True
            return
        self.body.pop(0)
        if (headx, heady) in self.body:
            self.dead: bool = True
            return
        self.body.append((headx, heady))
        self.can_change_direction: bool = True
