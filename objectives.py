import pygame
import os
from pygame.math import Vector2
from config import *


class Counter():
    def __init__(self):
        self.value = 0
        self.base_font = pygame.font.Font(os.path.join("resources", "fonts", "PixeloidSans-Bold.ttf"), 30)
        self.transparent_surface = pygame.Surface((310, TILE_SIZE * 4), pygame.SRCALPHA)
        self.transparent_surface.fill((0, 0, 0, 200))
        self.transparent_rect = pygame.Rect(TILE_SIZE, WINDOW_HEIGHT - TILE_SIZE * 7, 310, TILE_SIZE * 4)
        self.header = self.base_font.render("Access cards:", True, (198, 189, 0))

    def draw(self, screen):
        screen.blit(self.transparent_surface, self.transparent_rect)
        screen.blit(self.header, ((self.transparent_rect.centerx) - (self.header.get_width() / 2), WINDOW_HEIGHT - TILE_SIZE * 6))
        number = str(self.value) + "/3"
        number_text = self.base_font.render(number, True, (198, 189, 0))
        screen.blit(number_text, ((self.transparent_rect.centerx) - (number_text.get_width() / 2), WINDOW_HEIGHT - TILE_SIZE * 5 + 10))


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