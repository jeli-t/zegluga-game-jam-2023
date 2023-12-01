import pygame
from config import *

class Player():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = (x, y, 10, 10)


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= 10
        if keys[pygame.K_d]:
            self.x += 10
        if keys[pygame.K_w]:
            self.y -= 10
        if keys[pygame.K_s]:
            self.y += 10

        self.rect = (self.x, self.y, TILL_SIZE, TILL_SIZE)


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)