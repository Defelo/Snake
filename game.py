import random
from typing import Tuple, Set

try:
    from snake import Snake
except ImportError:
    Snake = None


class Game:
    def __init__(self, width: int, height: int, snake: Snake):
        self.width: int = width
        self.height: int = height
        self.snake: Snake = snake
        self.register_snake()
        self.tick_counter: int = 0
        self.apples: Set[Tuple[int, int]] = set()

    def register_snake(self):
        assert self.width > 4 and self.height > 2, "Board is too small."
        self.snake.register(self, [(2 + i, 2) for i in range(3)])

    def eat_apple(self, x: int, y: int):
        if (x, y) in self.apples:
            self.apples.remove((x, y))
            return True
        return False

    def tick(self):
        if self.tick_counter % 20 == 0 and len(self.apples) < len(self.snake.body):
            self.apples.add((random.randint(0, self.width - 1), random.randint(0, self.height - 1)))
        self.snake.tick()
        self.tick_counter += 1
