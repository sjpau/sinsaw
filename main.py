import sys
import pygame
from states.menu import Menu
from states.over import GameOver
from states.splash import Splash
from states.gameplay import Gameplay
from game import Game
import screen as s


pygame.init()
screen = pygame.display.set_mode((s.width, s.height), pygame.RESIZABLE)
states = {
    "MENU": Menu(),
    "SPLASH": Splash(),
    "GAMEPLAY": Gameplay("example.json"),
    "GAME_OVER": GameOver(),
}

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
sys.exit()