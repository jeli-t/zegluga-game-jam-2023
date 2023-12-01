import pygame
import sys
from config import *
from player import *
from level import *

# Initialize Pygame
pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Plague")
        self.level = Level()
        self.camera = Camera()
        self.player = Player()
        self.main_loop()


    def render(self):
        self.screen.fill((0, 0, 0))
        self.level.render(self.screen, self.camera)
        self.player.draw(self.screen, self.camera)
        pygame.display.update()


    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.player.move()
            self.camera.update(self.player)
            self.render()
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    Game()