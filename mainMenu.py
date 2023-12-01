import pygame, os
from config import *

class MainMenu:
    def __init__(self):
        self.font = pygame.font.Font(os.path.join("resources", "fonts", "PixeloidSans-Bold.ttf"), 40)
        self.fontImg = self.font.render(GAME_TITLE, True, (255, 255, 255))
        
    def draw(self, screen):
        screen.fill((50, 50, 60))
        screen.blit(self.fontImg, ((WINDOW_WIDTH / 2) - (self.fontImg.get_width() / 2), 20))