import pygame
import math
from pygame.math import Vector2
from config import *

class Zombie():
    def __init__(self, x, y, health):
        self.health = health
        self.position = Vector2(x, y)
        self.rect = pygame.Rect(self.position.x, self.position.y, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = 2
        self.attack_arrea = 4
        self.direction = 'left'
        self.moving = False
        self.current_animation = "idle"
        self.load_animation(self.current_animation)


    def load_animation(self, animation_name):
        # "animation_name":["path_to_assets", number_of_assets, frame_duration]
        animations = {"idle":["resources\zombie_idle\idle.png", 3, 700],
                    "walk":["resources\zombie_walk\walk.png", 7, 200],
                    "attack":["resources\zombie_attack\\attack.png", 5, 100],
                    "death":["resources\zombie_death\death.png", 4, 200]}
        image = pygame.image.load(animations[animation_name][0]).convert_alpha()
        if self.direction == 'left':
            image = pygame.transform.flip(image, True, False)
        self.frames_number = animations[animation_name][1]
        self.frames = [pygame.transform.scale(image.subsurface((i * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE)), (PLAYER_SIZE, PLAYER_SIZE)) for i in range(self.frames_number)]
        self.frame_duration = animations[animation_name][2]
        self.current_frame = 0
        self.last_frame_change = pygame.time.get_ticks()


    def move(self, target, camera, map):
        previous_position = [self.rect.x, self.rect.y]
        previous_direction = self.direction
    
        distance = math.sqrt((self.rect.centerx - target.position.x)**2 + (self.rect.centery - target.position.y)**2)
        if distance / 100 < self.attack_arrea:
            if self.current_animation == "idle":
                self.current_animation = "walk"
                self.load_animation("walk")
            direction = target.position + Vector2(PLAYER_SIZE / 2, PLAYER_SIZE / 2) - pygame.math.Vector2(self.rect.center)
            try:
                direction.normalize_ip()
            except ValueError:
                pass

            if direction.x < 0:
                self.test_collisions(pygame.Rect(self.rect.x - camera.position.x - self.speed, self.rect.y - camera.position.y, PLAYER_SIZE, PLAYER_SIZE), map.hard_tiles)
                if not self.collisions['left']:
                    self.rect.x -= self.speed
                    self.direction = 'left'
            elif direction.x > 0:
                self.test_collisions(pygame.Rect(self.rect.x - camera.position.x + self.speed, self.rect.y - camera.position.y, PLAYER_SIZE, PLAYER_SIZE), map.hard_tiles)
                if not self.collisions['right']:
                    self.rect.x += self.speed
                    self.direction = 'right'
            if direction.y < 0:
                self.test_collisions(pygame.Rect(self.rect.x - camera.position.x, self.rect.y - camera.position.y - self.speed, PLAYER_SIZE, PLAYER_SIZE), map.hard_tiles)
                if not self.collisions['top']:
                    self.rect.y -= self.speed
            elif direction.y > 0:
                self.test_collisions(pygame.Rect(self.rect.x - camera.position.x, self.rect.y - camera.position.y + self.speed, PLAYER_SIZE, PLAYER_SIZE), map.hard_tiles)
                if not self.collisions['bottom']:
                    self.rect.y += self.speed
        else:
            if self.current_animation == "walk":
                self.current_animation = "idle"
                self.load_animation("idle")

        # change animations depending on movement
        if previous_position[0] == self.rect.x and previous_position[1] == self.rect.y:
            if self.moving:
                self.current_animation = "idle"
                self.load_animation("idle")
                self.moving = False
        else:
            if previous_direction is not self.direction:
                self.load_animation("walk")
            if not self.moving:
                self.current_animation = "walk"
                self.load_animation("walk")
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
        screen.blit(self.frames[self.current_frame], (self.rect.x - camera.position.x, self.rect.y - camera.position.y, PLAYER_SIZE, PLAYER_SIZE))