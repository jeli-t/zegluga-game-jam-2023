import pygame
from pygame.math import Vector2
from config import *


class Camera():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

    def update(self, player):
        self.rect.x = player.rect.x - (WINDOW_WIDTH // 2)
        self.rect.y = player.rect.y - (WINDOW_HEIGHT // 2)
        print(self.rect)