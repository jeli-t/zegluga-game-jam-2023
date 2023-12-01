import pygame
from config import *

class Player():
    def __init__(self):
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(WINDOW_WIDTH // 2 - TILE_SIZE // 2, WINDOW_HEIGHT // 2 - TILE_SIZE // 2, TILE_SIZE, TILE_SIZE)


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10
        if keys[pygame.K_w]:
            self.rect.y -= 10
        if keys[pygame.K_s]:
            self.rect.y += 10


    def draw(self, screen, camera):
        pygame.draw.rect(screen, self.color, (self.rect.x - camera.position.x, self.rect.y - camera.position.y, TILE_SIZE, TILE_SIZE))