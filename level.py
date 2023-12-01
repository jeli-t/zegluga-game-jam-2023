import pygame
from pygame.math import Vector2
from pytmx.util_pygame import load_pygame
from config import *

pygame.init()


class Camera():
    def __init__(self):
        self.position = Vector2(0, 0)

    def update(self, player):
        self.position.x = player.rect.x - (WINDOW_WIDTH // 2)
        self.position.y = player.rect.y - (WINDOW_HEIGHT // 2)


class Room(pygame.sprite.Sprite):
    def __init__(self, offset, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.offset = offset
        self.position = self.offset
        self.rect = self.image.get_rect(topleft = self.position)

    def update(self, camera):
        self.position = Vector2(self.offset.x - camera.position.x, self.offset.y - camera.position.y)
        self.rect = self.image.get_rect(topleft = self.position)


class Map():
    def __init__(self, file='maps/SampleMap.tmx'):
        self.tile_group = pygame.sprite.Group()
        self.rooms = self.load_level(file)

    def render(self, screen, camera):
        self.tile_group.update(camera)
        self.tile_group.draw(screen)

    def load_level(self, file='maps/SampleMap.tmx'):
        tmx_data = load_pygame(file)
        for layer in tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x,y,surf in layer.tiles():
                    offset = Vector2(x*TILE_SIZE, y*TILE_SIZE)
                    Room(offset = offset, surf = surf, groups = self.tile_group)


class Level():
    def __init__(self):
        self.map = Map()

    def render(self, screen, camera):
        self.map.render(screen, camera)