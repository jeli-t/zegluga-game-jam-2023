import pygame
import sys
from config import *
from player import *
from level import *
from menu import *

# Initialize Pygame
pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.level = Level()
        self.camera = Camera()
        self.player = Player()
        self.hud = Hud(self.player)
        if not DEV:
            MainMenu(self.screen)
        self.game_over_screen = GameOver()
        self.game_over = False
        self.main_loop()


    def render(self):
        self.screen.fill((0, 0, 0))
        self.level.render(self.screen, self.camera)
        self.player.draw(self.screen, self.camera)
        if self.game_over:
            self.game_over_screen.render(self.screen)
            if self.game_over_screen.start_btn.draw(self.screen):
                self.level = Level()
                self.camera = Camera()
                self.player = Player()
                self.hud = Hud(self.player)
                self.game_over_screen = GameOver()
                self.game_over = False
        else:
            self.hud.draw(self.screen)
        pygame.display.update()


    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.player.health <= 0:
                self.game_over = True

            if not self.game_over:
                self.player.move()
                self.camera.update(self.player)
                self.hud.update()
            self.render()
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    Game()