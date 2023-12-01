import pygame, os
from config import *
from button import *
from player import *
from level import *


class GameOver:
    def __init__(self):
        self.base_font = pygame.font.Font(os.path.join("resources", "fonts", "PixeloidSans-Bold.ttf"), 60)
        self.outline_font = pygame.font.Font(os.path.join("resources", "fonts", "PixeloidSans-Bold.ttf"), 61)
        self.transparent_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.transparent_surface.fill((0, 0, 0, 200))
        self.transparent_rect = self.transparent_surface.get_rect()
        self.font_img = self.base_font.render("GAME OVER", True, (198, 189, 0))
        self.font_img_glow = self.outline_font.render("GAME OVER", True, (11, 11, 11))
        self.start_btn = Button(WINDOW_WIDTH / 2, 440, "Restart", 40)

    def render(self, screen):
        screen.blit(self.transparent_surface, self.transparent_rect)
        screen.blit(self.font_img_glow, ((WINDOW_WIDTH / 2) - (self.font_img_glow.get_width() / 2) - 5, 280))
        screen.blit(self.font_img, ((WINDOW_WIDTH / 2) - (self.font_img.get_width() / 2), 270))


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.base_font = pygame.font.Font(os.path.join("resources", "fonts", "PixeloidSans-Bold.ttf"), 60)
        self.outline_font = pygame.font.Font(os.path.join("resources", "fonts", "PixeloidSans-Bold.ttf"), 61)
        self.font_img = self.base_font.render(GAME_TITLE, True, (198, 189, 0))
        self.font_img_glow = self.outline_font.render(GAME_TITLE, True, (11, 11, 11))
        self.start_btn = Button(WINDOW_WIDTH / 2, 440, "Start", 40)
        self.exit_btn = Button(WINDOW_WIDTH / 2, 530, "Exit", 40)
        self.menu_loop()

    def menu_loop(self):
        while True:

            self.screen.fill((30, 30, 30))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.start_btn.draw(self.screen):
                break
            if self.exit_btn.draw(self.screen):
                pygame.quit()
                exit(0)

            self.screen.blit(self.font_img_glow, ((WINDOW_WIDTH / 2) - (self.font_img_glow.get_width() / 2) - 5, 280))
            self.screen.blit(self.font_img, ((WINDOW_WIDTH / 2) - (self.font_img.get_width() / 2), 270))
            pygame.display.update()