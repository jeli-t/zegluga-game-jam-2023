import pygame, os
from config import *
from button import *

class MainMenu:
    def __init__(self):
        self.font = pygame.font.Font(os.path.join("resources", "fonts", "PixeloidSans-Bold.ttf"), 40)
        self.fontImg = self.font.render(GAME_TITLE, True, (255, 255, 255))
        self.startBtnImg = pygame.image.load("resources/startBtn.png").convert_alpha()
        self.startBtn = Button((WINDOW_WIDTH / 2) - (self.startBtnImg.get_width() / 2), 70, self.startBtnImg, "Start", 1)
        
    def draw(self, screen):
        screen.fill((30, 30, 30))
        screen.blit(self.fontImg, ((WINDOW_WIDTH / 2) - (self.fontImg.get_width() / 2), 20))
        if self.startBtn.draw(screen):
            exit(0)