import pygame
from pygame.math import Vector2
from config import *

class Zombie():
    def __init__(self, x, y, health):
        self.health = health
        self.position = Vector2(x, y)
        self.rect = pygame.Rect(self.position.x, self.position.y, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = 5
        self.direction = 'left'
        self.moving = False
        self.current_animation = "idle"
        self.load_animation(self.current_animation)


    def load_animation(self, animation_name):
        # "animation_name":["path_to_assets", number_of_assets, frame_duration]
        animations = {"idle":["resources\zombie_idle\idle.png", 3, 700],
                    "walk":["resources\zombie_walk\walk.png", 7, 200],
                    "attack":["resources\zombie_attack\\attack.png", 5, 300]}
        image = pygame.image.load(animations[animation_name][0]).convert_alpha()
        if self.direction == 'left':
            image = pygame.transform.flip(image, True, False)
        self.frames_number = animations[animation_name][1]
        self.frames = [pygame.transform.scale(image.subsurface((i * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE)), (PLAYER_SIZE, PLAYER_SIZE)) for i in range(self.frames_number)]
        self.frame_duration = animations[animation_name][2]
        self.current_frame = 0
        self.last_frame_change = pygame.time.get_ticks()


    def draw(self, screen, camera):
        now = pygame.time.get_ticks()
        if now - self.last_frame_change > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.frames_number
            self.last_frame_change = now
        screen.blit(self.frames[self.current_frame], (self.position.x - camera.position.x, self.position.y - camera.position.y, PLAYER_SIZE, PLAYER_SIZE))