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
        self.image = pygame.transform.scale(surf, (TILE_SIZE * 2, TILE_SIZE * 2))
        self.offset = offset
        self.position = self.offset
        self.rect = self.image.get_rect(topleft = self.position)

    def update(self, camera):
        self.position = Vector2(self.offset.x - camera.position.x, self.offset.y - camera.position.y)
        self.rect = self.image.get_rect(topleft = self.position)


class Map():
    def __init__(self, file='maps/main_floor.tmx'):
        self.soft_tiles = pygame.sprite.Group()     # tiles that do not collide with the player
        self.hard_tiles = pygame.sprite.Group()     # tiles that collide with the player
        self.rooms = self.load_level(file)

    def render(self, screen, camera):
        self.soft_tiles.update(camera)
        self.soft_tiles.draw(screen)
        self.hard_tiles.update(camera)
        self.hard_tiles.draw(screen)

    def load_level(self, file='maps/main_floor.tmx'):
        tmx_data = load_pygame(file)
        for layer in tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x,y,surf in layer.tiles():
                    offset = Vector2(x * TILE_SIZE * 2, y * TILE_SIZE * 2)
                    if layer.name == 'walls':
                        Room(offset = offset, surf = surf, groups = self.hard_tiles)
                    if layer.name == 'floor':
                        Room(offset = offset, surf = surf, groups = self.soft_tiles)


class Level():
    def __init__(self):
        self.map = Map()

    def render(self, screen, camera):
        self.map.render(screen, camera)