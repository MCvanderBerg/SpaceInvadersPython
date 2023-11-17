from Missle import Missle
from Constants import SCREEN_HEIGHT, CLEAR, screen
from pygame import Rect, draw
from  random import randint

class Missles:
    def __init__(self):
        self.missles = []

    def add(self, x, y):
        if randint(0,1000) <= 1:
            self.missles.append(Missle(x, y, True))

    def update(self):
        if self.missles:
            for m in reversed(range(len(self.missles))):
                if self.missles[m].y >= SCREEN_HEIGHT:
                    del self.missles[m]
                else:
                    self.missles[m].update()


    def clear(self):
        for m in reversed(range(len(self.missles))):
            draw.rect(screen, CLEAR, Rect(self.missles[m].x, self.missles[m].y, self.missles[m].width, self.missles[m].height))

    def print(self):
        for m in reversed(range(len(self.missles))):
            self.missles[m].print()
