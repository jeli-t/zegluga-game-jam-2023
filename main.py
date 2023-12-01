import pygame
import sys
from config import *

# Initialize Pygame
pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Plague")
        self.main_loop()


    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    Game()