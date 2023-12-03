import pygame
import sys
from config import *
from player import *
from level import *
from menu import *
from zombie import *
from objectives import *

# Initialize Pygame
pygame.init()

# Initialize the Pygame Music Mixer
pygame.mixer.init()
# # Play the music in an infinite loop
mainMusic = pygame.mixer.Sound(os.path.join("resources", "music", "CrisisCorridor.mp3"))
mainMusic.set_volume(0.7)
pygame.mixer.Channel(0).play(mainMusic, -1)

class Game:
    def __init__(self):
        self.zombieChannel = pygame.mixer.Channel(1)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.level = Level()
        self.camera = Camera()
        self.player = Player(self.level.player_spawn)
        self.zombies = []
        self.init_zombies()
        self.potions = []
        self.init_potions()
        self.cards = []
        self.init_cards()
        self.health_bar = HealthBar(self.player)
        self.counter = Counter()
        self.instruction = Instruction()
        if not DEV:
            MainMenu(self.screen)
        self.game_over_screen = GameOver()
        self.win_screen = WinScreen()
        self.game_over = False
        self.main_loop()


    def init_zombies(self):
        for spawn_point in self.level.zombie_spawns:
            zombie = Zombie(spawn_point.x * TILE_SIZE * 2, spawn_point.y * TILE_SIZE * 2, 100)
            self.zombies.append(zombie)


    def init_potions(self):
        for potion_position in self.level.potions:
            potion = Potion(potion_position.x * TILE_SIZE * 2, potion_position.y * TILE_SIZE * 2)
            self.potions.append(potion)

    def init_cards(self):
        for card_position in self.level.cards:
            card = Card(card_position.x * TILE_SIZE * 2, card_position.y * TILE_SIZE * 2)
            self.cards.append(card)


    def restart(self):
        self.level = Level()
        self.camera = Camera()
        self.player = Player(self.level.player_spawn)
        self.zombies = []
        self.init_zombies()
        self.potions = []
        self.init_potions()
        self.cards = []
        self.init_cards()
        self.health_bar = HealthBar(self.player)
        self.counter = Counter()
        self.game_over_screen = GameOver()
        self.win_screen = WinScreen()
        self.game_over = False


    def render(self):
        self.screen.fill((66, 59, 77))
        self.level.render(self.screen, self.camera)
        self.player.draw(self.screen, self.camera)
        self.instruction.draw(self.screen, self.camera)
        for zombie in self.zombies:
            zombie.draw(self.screen, self.camera)
        for potion in self.potions:
            potion.draw(self.screen, self.camera)
        for card in self.cards:
            card.draw(self.screen, self.camera)
        if self.game_over:
            self.game_over_screen.render(self.screen)
            if self.game_over_screen.start_btn.draw(self.screen):
                self.restart()
            if self.game_over_screen.exit_btn.draw(self.screen):
                pygame.quit()
                sys.exit()
        else:
            self.counter.draw(self.screen)
            self.health_bar.draw(self.screen)
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

            for zombie in self.zombies:
                zombie.move(self.player, self.camera)
                if zombie.rect.colliderect(pygame.Rect(self.player.position.x, self.player.position.y, PLAYER_SIZE, PLAYER_SIZE)):
                    if zombie.current_animation != "attack":
                        zombie.current_animation = "attack"
                        zombie.load_animation("attack")
                        self.zombieChannel.play(pygame.mixer.Sound(os.path.join("resources", "music", "ZombieAttack.mp3")), -1)
                    self.player.health -= 1
                else:
                    if zombie.current_animation == "attack":
                        zombie.current_animation = "idle"
                        zombie.load_animation("idle")
                        self.zombieChannel.stop()

            for potion in self.potions:
                if potion.rect.colliderect(pygame.Rect(self.player.position.x, self.player.position.y, PLAYER_SIZE, PLAYER_SIZE)):
                    self.player.health += 50
                    if self.player.health > 228:
                        self.player.health = 228
                    self.potions.remove(potion)

            for card in self.cards:
                if card.rect.colliderect(pygame.Rect(self.player.position.x, self.player.position.y, PLAYER_SIZE, PLAYER_SIZE)):
                    self.counter.value += 1
                    self.cards.remove(card)

            if self.player.health <= 0:
                self.cutscene = True
                self.player.current_animation = "death"
                self.player.load_animation("death")
                self.game_over = True

            if not self.game_over:
                self.player.move(self.level.map)
                self.camera.update(self.player)
                self.health_bar.update()
            else:
                self.zombieChannel.stop()

            self.render()
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    Game()