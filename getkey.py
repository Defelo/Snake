import sys
import termios
import tty


def getkey() -> str:
    def gk() -> str:
        fd: int = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch: str = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    out: str = gk()
    if out == "\033":
        o: str = gk()
        if o == "[":
            return out + o + gk()
        return out + o
    return out
