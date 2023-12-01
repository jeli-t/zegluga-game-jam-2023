import pygame, os
from config import *
from button import *

class MainMenu:
    def __init__(self):
        self.font = pygame.font.Font(os.path.join("resources", "fonts", "PixeloidSans-Bold.ttf"), 40)
        self.fontImg = self.font.render(GAME_TITLE, True, (255, 255, 255))
        self.start_btn_img = pygame.image.load("resources/button.png").convert_alpha()
        self.start_btn = Button((WINDOW_WIDTH / 2) - (self.start_btn_img.get_width() / 2), 70, self.start_btn_img, "Start", 1)
        
    def draw(self, screen):
        screen.fill((30, 30, 30))
        screen.blit(self.fontImg, ((WINDOW_WIDTH / 2) - (self.fontImg.get_width() / 2), 20))
        if self.start_btn.draw(screen):
            exit(0)