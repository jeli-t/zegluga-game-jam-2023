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
            self.position.x -= 10
            colliding_tiles = pygame.sprite.spritecollide(self, map.hard_tiles, dokill=False)
            # Determine the player position whe colliding - left or right of the tile
            # If we are on the left side, continue normal left movement
            if colliding_tiles and self.rect.x >= colliding_tiles[0].rect.x + colliding_tiles[0].rect.width / 2:
                # Otherwise we need to prevent the player from going further
                offset = colliding_tiles[0].rect.x + colliding_tiles[0].rect.width - self.rect.x
                self.position.x += offset
            else:
                self.direction = 'left'
        if keys[pygame.K_d]:
            self.position.x += 10
            colliding_tiles = pygame.sprite.spritecollide(self, map.hard_tiles, dokill=False)
            # Determine the player position whe colliding - left or right of the tile
            # If we are on the right side, continue normal left movement
            if colliding_tiles and self.rect.x <= colliding_tiles[0].rect.x + colliding_tiles[0].rect.width / 2:
                # Otherwise we need to prevent the player from going further
                offset = (TILE_SIZE * 2) - ((colliding_tiles[0].rect.x + colliding_tiles[0].rect.width - self.rect.x) % (TILE_SIZE * 2))
                self.position.x -= offset
            else:
                self.direction = 'right'
        if keys[pygame.K_w]:
            self.position.y -= 10
            colliding_tiles = pygame.sprite.spritecollide(self, map.hard_tiles, dokill=False)
            # Determine the player position whe colliding - top or bottom of the tile
            # If we are on the top side, continue normal top movement
            if colliding_tiles and self.rect.y + self.rect.height / 2 <= colliding_tiles[0].rect.y + colliding_tiles[0].rect.height:
                # Otherwise we need to prevent the player from going further
                offset = (TILE_SIZE * 2) - ((colliding_tiles[0].rect.y + colliding_tiles[0].rect.height - (self.rect.y)) % (TILE_SIZE * 2))
                self.position.y += offset
        if keys[pygame.K_s]:
            self.position.y += 10
            colliding_tiles = pygame.sprite.spritecollide(self, map.hard_tiles, dokill=False)
            # Determine the player position whe colliding - left or right of the tile
            # If we are on the bottom side, continue normal left movement
            if colliding_tiles and self.rect.y + self.rect.height <= colliding_tiles[0].rect.y + colliding_tiles[0].rect.height / 2:
                # Otherwise we need to prevent the player from going further
                print("Top")
                # offset = (TILE_SIZE * 2) - ((colliding_tiles[0].rect.y + colliding_tiles[0].rect.height - self.rect.y) % (TILE_SIZE * 2))
                # self.position.y -= offset
        if keys[pygame.K_r]:
            self.health -= 10

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


    def draw(self, screen, camera):
        now = pygame.time.get_ticks()
        if now - self.last_frame_change > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % self.frames_number
            self.last_frame_change = now
        screen.blit(self.frames[self.current_frame], (self.rect.x, self.rect.y, TILE_SIZE * 4, TILE_SIZE * 4))