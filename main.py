import sys
import pygame
import screen as s
pygame.init()
screen = pygame.display.set_mode((s.width, s.height), pygame.RESIZABLE)
from states.menu import Menu
from states.over import GameOver
from states.splash import Splash
from states.gameplay import Gameplay
from game import Game
import finals

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.music.load(finals.music_path + 'night_shift.ogg')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
states = {
    "MENU": Menu(screen),
    "SPLASH": Splash(screen),
    "GAMEPLAY": Gameplay(finals.chapters['The Night Shift'], screen),
}

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
sys.exit()