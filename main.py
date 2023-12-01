import pygame
import sys
from config import *
from player import *
# Initialize Pygame
pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Plague")
        self.player = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, (255,0,0))
        self.main_loop()


    def render(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        pygame.display.update()


    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.player.move()
            self.render()
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    Game()