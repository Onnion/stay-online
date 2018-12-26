import autopy
import threading
import random


def setInterval(func, time):
    e = threading.Event()
    while not e.wait(time):
        func()


def move():
    x = random.randint(100,300)
    y = random.randint(100,300)
    autopy.mouse.smooth_move(x, y)


setInterval(move, 5)
