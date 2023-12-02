import pygame
import sys
from config import *
from player import *
from level import *
from menu import *
from zombie import *

# Initialize Pygame
pygame.init()

# Initialize the Pygame Music Mixer
pygame.mixer.init()
# Load the main music
pygame.mixer.music.load(os.path.join("resources", "music", "CrisisCorridor.mp3"), "mp3")
# Play the music in an infinite loop
pygame.mixer.music.play(-1)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.level = Level()
        self.camera = Camera()
        self.player = Player(self.level.player_spawn)
        self.zombies = []
        self.init_zombies()
        self.hud = Hud(self.player)
        if not DEV:
            MainMenu(self.screen)
        self.game_over_screen = GameOver()
        self.game_over = False
        self.main_loop()


    def init_zombies(self):
        zombie = Zombie(100, 0, 100)
        self.zombies.append(zombie)
        zombie = Zombie(200, 0, 100)
        zombie.current_animation = "walk"
        zombie.load_animation("walk")
        self.zombies.append(zombie)
        zombie = Zombie(300, 0, 100)
        zombie.current_animation = "attack"
        zombie.load_animation("attack")
        self.zombies.append(zombie)


    def restart(self):
        self.level = Level()
        self.camera = Camera()
        self.player = Player()
        self.hud = Hud(self.player)
        self.game_over_screen = GameOver()
        self.game_over = False


    def render(self):
        self.screen.fill((66, 59, 77))
        self.level.render(self.screen, self.camera)
        self.player.draw(self.screen, self.camera)
        for zombie in self.zombies:
            zombie.draw(self.screen, self.camera)
        if self.game_over:
            self.game_over_screen.render(self.screen)
            if self.game_over_screen.start_btn.draw(self.screen):
                self.restart()
            if self.game_over_screen.exit_btn.draw(self.screen):
                pygame.quit()
                sys.exit()
        else:
            self.hud.draw(self.screen)
        pygame.display.update()


    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and not self.game_over:
                        if DEV:
                            pygame.quit()
                            sys.exit()
                        else:
                            InGameMenu(self.screen)

            if self.player.health <= 0:
                self.cutscene = True
                self.player.current_animation = "death"
                self.player.load_animation("death")
                self.game_over = True

            if not self.game_over:
                self.player.move(self.level.map)
                self.camera.update(self.player)
                self.hud.update()

            self.render()
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    Game()