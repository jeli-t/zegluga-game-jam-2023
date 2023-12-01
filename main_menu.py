import pygame, os
from config import *
from button import *

class MainMenu:
    def __init__(self):
        self.base_font = pygame.font.Font(os.path.join("resources", "fonts", "PixeloidSans-Bold.ttf"), 60)
        self.outline_font = pygame.font.Font(os.path.join("resources", "fonts", "PixeloidSans-Bold.ttf"), 61)
        self.font_img = self.base_font.render(GAME_TITLE, True, (198, 189, 0))
        self.font_img_glow = self.outline_font.render(GAME_TITLE, True, (11, 11, 11))
        self.btn_img = pygame.image.load("resources/button.png").convert_alpha()
        self.start_btn = Button(WINDOW_WIDTH / 2, 440, "Start", 40)
        self.exit_btn = Button(WINDOW_WIDTH / 2, 530, "Exit", 40)
        
    def draw(self, screen):
        screen.fill((30, 30, 30))
        screen.blit(self.font_img_glow, ((WINDOW_WIDTH / 2) - (self.font_img_glow.get_width() / 2) - 5, 280))
        screen.blit(self.font_img, ((WINDOW_WIDTH / 2) - (self.font_img.get_width() / 2), 270))
        if self.start_btn.draw(screen):
            exit(0)
        if self.exit_btn.draw(screen):
            exit(0)