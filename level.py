import pygame
from pygame.math import Vector2
from config import *


class Camera():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

    def update(self, player):
        self.rect.x = player.rect.x - (WINDOW_WIDTH // 2)
        self.rect.y = player.rect.y - (WINDOW_HEIGHT // 2)


class Room():
    def __init__(self, x, y):
        self.position = Vector2(x, y) # relative to other rooms
        self.color = (0, 100, 100)
        self.rect = pygame.Rect(self.position.x * TILE_SIZE, self.position.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def draw(self, screen, camera):
        self.rect = pygame.Rect(self.position.x * TILE_SIZE - camera.rect.x, self.position.y * TILE_SIZE - camera.rect.y, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, self.color, self.rect)


class Map():
    def __init__(self):
        self.rooms = []

    def render(self, screen, camera):
        for room in self.rooms:
            room.draw(screen, camera)

    def sample(self):
        room = Room(0,0)
        self.rooms.append(room)
        room = Room(1,1)
        self.rooms.append(room)
        room = Room(2,2)
        self.rooms.append(room)
        room = Room(3,3)
        self.rooms.append(room)
        room = Room(4,4)
        self.rooms.append(room)
        room = Room(5,5)
        self.rooms.append(room)
        room = Room(6,6)
        self.rooms.append(room)
        room = Room(7,7)
        self.rooms.append(room)
        


class Level():
    def __init__(self):
        self.map = Map()
        self.map.sample()

    def render(self, screen, camera):
        self.map.render(screen, camera)