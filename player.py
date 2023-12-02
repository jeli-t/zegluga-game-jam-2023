import pygame
from pygame.math import Vector2
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
        self.position = Vector2(WINDOW_WIDTH // 2 - TILE_SIZE // 2, WINDOW_HEIGHT // 2 - TILE_SIZE // 2)
        self.rect = pygame.Rect(self.position.x, self.position.y, TILE_SIZE * 4, TILE_SIZE * 4)
        self.direction = 'left'
        self.moving = False
        self.speed = 10
        self.collisions = {'left' : False, 'right' : False, 'top' : False, 'bottom' : False}
        self.current_animation = "idle"
        self.load_animation(self.current_animation)


    def load_animation(self, animation_name):
        # "animation_name":["path_to_assets", number_of_assets, frame_duration]
        animations = {"idle":["resources\player_idle\idle.png", 2, 500],
                    "run":["resources\player_run\\run_fix.png", 7, 50],
                    "death":["resources\player_death\death.png", 4, 600]}
        image = pygame.image.load(animations[animation_name][0]).convert_alpha()
        if self.direction == 'left':
            image = pygame.transform.flip(image, True, False)
        self.frames_number = animations[animation_name][1]
        self.frames = [pygame.transform.scale(image.subsurface((i * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE)), (TILE_SIZE * 4, TILE_SIZE * 4)) for i in range(self.frames_number)]
        self.frame_duration = animations[animation_name][2]
        self.current_frame = 0
        self.last_frame_change = pygame.time.get_ticks()


    def move(self, map):
        keys = pygame.key.get_pressed()

        pos = [self.position.x, self.position.y]
        direction = self.direction

        if keys[pygame.K_a]:
            self.test_collisions(pygame.Rect(self.rect.x - self.speed, self.rect.y, TILE_SIZE * 4, TILE_SIZE * 4), map.hard_tiles)
            if not self.collisions['left']:
                self.position.x -= self.speed
                self.direction = 'left'
        if keys[pygame.K_d]:
            self.test_collisions(pygame.Rect(self.rect.x + self.speed, self.rect.y, TILE_SIZE * 4, TILE_SIZE * 4), map.hard_tiles)
            if not self.collisions['right']:
                self.position.x += self.speed
                self.direction = 'right'
        if keys[pygame.K_w]:
            self.test_collisions(pygame.Rect(self.rect.x, self.rect.y - self.speed, TILE_SIZE * 4, TILE_SIZE * 4), map.hard_tiles)
            if not self.collisions['top']:
                self.position.y -= self.speed
        if keys[pygame.K_s]:
            self.test_collisions(pygame.Rect(self.rect.x, self.rect.y + self.speed, TILE_SIZE * 4, TILE_SIZE * 4), map.hard_tiles)
            if not self.collisions['bottom']:
                self.position.y += self.speed
        if keys[pygame.K_r]:
            self.health -= 3

        # change animations depending on movement
        if pos[0] == self.position.x and pos[1] == self.position.y:
            if self.moving:
                self.current_animation = "idle"
                self.load_animation("idle")
                self.moving = False
        else:
            if direction is not self.direction:
                self.load_animation("run")
            if not self.moving:
                self.current_animation = "run"
                self.load_animation("run")
                self.moving = True


    def test_collisions(self, hit_box, tiles):
        self.collisions = {'left' : False, 'right' : False, 'top' : False, 'bottom' : False}
        for tile in tiles:
            if hit_box.colliderect(tile.rect):
                if hit_box.x <= tile.rect.x:
                    self.collisions['right'] = True
                if hit_box.x >= tile.rect.x:
                    self.collisions['left'] = True
                if hit_box.y >= tile.rect.y:
                    self.collisions['top'] = True
                if hit_box.y <= tile.rect.y:
                    self.collisions['bottom'] = True


    def draw(self, screen, camera):
        now = pygame.time.get_ticks()
        if now - self.last_frame_change > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.frames_number
            self.last_frame_change = now
        screen.blit(self.frames[self.current_frame], (self.rect.x, self.rect.y, TILE_SIZE * 4, TILE_SIZE * 4))