import pygame, os
from config import *
from button import *

class MainMenu:
    def __init__(self):
        self.font = pygame.font.Font(os.path.join("resources", "fonts", "PixeloidSans-Bold.ttf"), 60)
        self.font_img = self.font.render(GAME_TITLE, True, (255, 255, 255))
        self.font_img_glow = self.font.render(GAME_TITLE, True, (130, 45, 255))
        self.btn_img = pygame.image.load("resources/button.png").convert_alpha()
        self.start_btn = Button((WINDOW_WIDTH / 2) - (self.btn_img.get_width() / 2), 420, self.btn_img, "Start", 1)
        self.exit_btn = Button((WINDOW_WIDTH / 2) - (self.btn_img.get_width() / 2), 530, self.btn_img, "Exit", 1)
        
    def draw(self, screen):
        screen.fill((30, 30, 30))
        screen.blit(self.font_img_glow, ((WINDOW_WIDTH / 2) - (self.font_img_glow.get_width() / 2), 275))
        screen.blit(self.font_img, ((WINDOW_WIDTH / 2) - (self.font_img.get_width() / 2), 270))
        if self.start_btn.draw(screen):
            exit(0)
        if self.exit_btn.draw(screen):
            exit(0)