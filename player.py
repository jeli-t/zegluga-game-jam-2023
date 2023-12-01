import pygame
from config import *


class Hud():
    def __init__(self, player):
        self.player = player
        self.health_bar_img = pygame.image.load("resources\health_bar.png")
        self.health_bar_img_rect = self.health_bar_img.get_rect()
        self.health_bar_img_rect.x = TILE_SIZE
        self.health_bar_img_rect.y = WINDOW_HEIGHT - TILE_SIZE * 3
        self.health_bar = pygame.Rect(TILE_SIZE, WINDOW_HEIGHT - TILE_SIZE * 3, self.player.health, TILE_SIZE * 2)

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), self.health_bar)
        screen.blit(self.health_bar_img, self.health_bar_img_rect)

    def update(self):
        self.health_bar = pygame.Rect(TILE_SIZE * 3 + 10, WINDOW_HEIGHT - TILE_SIZE * 3, self.player.health, TILE_SIZE * 2)


class Player():
    def __init__(self):
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(WINDOW_WIDTH // 2 - TILE_SIZE // 2, WINDOW_HEIGHT // 2 - TILE_SIZE // 2, TILE_SIZE, TILE_SIZE)
        self.health = 227


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
        if keys[pygame.K_r]:
            self.health -= 1


    def draw(self, screen, camera):
        pygame.draw.rect(screen, self.color, (self.rect.x - camera.position.x, self.rect.y - camera.position.y, TILE_SIZE, TILE_SIZE))