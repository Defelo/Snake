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

    def register_snake(self):
        assert self.width > 4 and self.height > 2, "Board is too small."
        self.snake.register(self, [(2 + i, 2) for i in range(3)])

    def tick(self):
        self.snake.tick()
