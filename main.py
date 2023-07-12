import sys
import pygame
import defs.screen as s
pygame.init()
screen = pygame.display.set_mode((s.width, s.height), pygame.RESIZABLE)
from states.menu import Menu
from states.over import GameOver
from states.splash import Splash
from states.gameplay import Gameplay
from game import Game
import defs.finals as finals

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.music.set_volume(0.4)
states = {
    "MENU": Menu(),
    "SPLASH": Splash(),
    #if it works it works..
    #it's a prototype anyways..right?
    "CHAPTER_NIGHT_SHIFT": Gameplay(finals.chapters['The Night Shift'], 'night_shift.ogg'),
    "CHAPTER_AFTERPARTY": Gameplay(finals.chapters['The Afterparty']),
    "CHAPTER_CARTE_BLANCHE": Gameplay(finals.chapters['Carte Blanche']),
}

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
sys.exit()
