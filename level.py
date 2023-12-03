import pygame
from pygame.math import Vector2
from pytmx.util_pygame import load_pygame
from config import *

pygame.init()


class Camera():
    def __init__(self):
        self.position = Vector2(0, 0)

    def update(self, player):
        self.position.x = player.position.x - (WINDOW_WIDTH // 2)
        self.position.y = player.position.y - (WINDOW_HEIGHT // 2)


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
    def __init__(self, level, file='maps/Map1.tmx'):
        self.level = level
        self.soft_tiles = pygame.sprite.Group()     # tiles that do not collide with the player
        self.hard_tiles = pygame.sprite.Group()     # tiles that collide with the player
        self.rooms = self.load_level(file)

    def render(self, screen, camera):
        self.soft_tiles.update(camera)
        self.soft_tiles.draw(screen)
        self.hard_tiles.update(camera)
        self.hard_tiles.draw(screen)

    def load_level(self, file='maps/Map1.tmx'):
        tmx_data = load_pygame(file)
        for layer in tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x,y,surf in layer.tiles():
                    offset = Vector2(x * TILE_SIZE * 2, y * TILE_SIZE * 2)
                    if layer.name == 'Walls':
                        Room(offset = offset, surf = surf, groups = self.hard_tiles)
                    elif layer.name == 'Collidable Assets':
                        Room(offset = offset, surf = surf, groups = self.hard_tiles)
                    elif layer.name == "Player Spawn":
                        self.level.player_spawn = Vector2(x, y)
                    elif layer.name == "Zombie Spawn":
                        self.level.zombie_spawns.append(Vector2(x, y))
                    elif layer.name == "Potions":
                        self.level.potions.append(Vector2(x, y))
                    elif layer.name == "Cards":
                        self.level.cards.append(Vector2(x, y))
                    elif layer.name == "Finish":
                        self.level.finish = (Vector2(x, y))
                        Room(offset = offset, surf = surf, groups = self.soft_tiles)
                    else:
                        Room(offset = offset, surf = surf, groups = self.soft_tiles)


class Level():
    def __init__(self):
        self.player_spawn = (0, 0)
        self.zombie_spawns = []
        self.potions = []
        self.cards = []
        self.finish = Vector2(0, 0)
        self.map = Map(self)

    def render(self, screen, camera):
        self.map.render(screen, camera)