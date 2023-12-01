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
        self.health = 227
        image = pygame.image.load("resources\player_idle\idle.png").convert_alpha()
        self.frames = [pygame.transform.scale(image.subsurface((i * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE)), (TILE_SIZE * 2, TILE_SIZE * 2)) for i in range(2)]
        self.rect = pygame.Rect(WINDOW_WIDTH // 2 - TILE_SIZE // 2, WINDOW_HEIGHT // 2 - TILE_SIZE // 2, TILE_SIZE * 2, TILE_SIZE * 2)
        self.current_frame = 0
        self.last_frame_change = pygame.time.get_ticks()
        self.frame_duration = 500


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
            self.health -= 10


    def draw(self, screen, camera):
        now = pygame.time.get_ticks()
        if now - self.last_frame_change > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % 2
            self.image = self.frames[self.current_frame]
            self.last_frame_change = now
        screen.blit(self.frames[self.current_frame], (self.rect.x - camera.position.x, self.rect.y - camera.position.y, TILE_SIZE, TILE_SIZE))