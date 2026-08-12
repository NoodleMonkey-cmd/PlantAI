import pygame
import random

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.uniform(-2, 2)
        self.dy = random.uniform(-5, -1)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = random.randint(2, 4)
        self.lifetime = 60

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.lifetime -= 1

    def draw(self, display):
        pygame.draw.circle(display, self.color, (int(self.x), int(self.y)), self.size)
