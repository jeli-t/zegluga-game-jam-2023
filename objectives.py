import pygame
from pygame.math import Vector2
from config import *


class Potion():
    def __init__(self, x, y):
        self.position = Vector2(x, y)
        self.rect = pygame.Rect(self.position.x, self.position.y, TILE_SIZE * 2, TILE_SIZE * 2)
        self.current_animation = "idle"
        self.load_animation(self.current_animation)


    def load_animation(self, animation_name):
        # "animation_name":["path_to_assets", number_of_assets, frame_duration]
        animations = {"idle":["resources\health_potion_anim.png", 4, 200]}
        image = pygame.image.load(animations[animation_name][0]).convert_alpha()
        self.frames_number = animations[animation_name][1]
        self.frames = [pygame.transform.scale(image.subsurface((i * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE)), (TILE_SIZE * 2, TILE_SIZE * 2)) for i in range(self.frames_number)]
        self.frame_duration = animations[animation_name][2]
        self.current_frame = 0
        self.last_frame_change = pygame.time.get_ticks()

    def draw(self, screen, camera):
        now = pygame.time.get_ticks()
        if now - self.last_frame_change > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.frames_number
            self.last_frame_change = now
        screen.blit(self.frames[self.current_frame], (self.rect.x - camera.position.x, self.rect.y - camera.position.y, TILE_SIZE * 2, TILE_SIZE * 2))


class Card():
    def __init__(self, x, y):
        self.position = Vector2(x, y)
        self.rect = pygame.Rect(self.position.x, self.position.y, TILE_SIZE * 2, TILE_SIZE * 2)
        self.current_animation = "idle"
        self.load_animation(self.current_animation)


    def load_animation(self, animation_name):
        # "animation_name":["path_to_assets", number_of_assets, frame_duration]
        animations = {"idle":["resources\card_anim.png", 4, 200]}
        image = pygame.image.load(animations[animation_name][0]).convert_alpha()
        self.frames_number = animations[animation_name][1]
        self.frames = [pygame.transform.scale(image.subsurface((i * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE)), (TILE_SIZE * 2, TILE_SIZE * 2)) for i in range(self.frames_number)]
        self.frame_duration = animations[animation_name][2]
        self.current_frame = 0
        self.last_frame_change = pygame.time.get_ticks()

    def draw(self, screen, camera):
        now = pygame.time.get_ticks()
        if now - self.last_frame_change > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.frames_number
            self.last_frame_change = now
        screen.blit(self.frames[self.current_frame], (self.rect.x - camera.position.x, self.rect.y - camera.position.y, TILE_SIZE * 2, TILE_SIZE * 2))