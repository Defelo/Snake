import time
from threading import Thread
from typing import Callable


class Timer(Thread):
    def __init__(self, interval: float, func: Callable):
        super().__init__()

        self.interval: float = interval
        self.func: Callable = func
        self.running: bool = False

    def run(self):
        self.running: bool = True
        time.sleep(self.interval)
        while self.running:
            self.func()
            time.sleep(self.interval)

    def stop(self):
        self.running: bool = False
