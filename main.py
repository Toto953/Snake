# LANCEMENT DU JEU

import pygame
from game import Game
from cryptography.fernet import Fernet
from os.path import exists

if not exists("key.key"):
    with open("key.key", "wb") as f:
        f.write(Fernet.generate_key())
if not exists("data.json"):
    f = open("data.json", "wb")
    f.close()

pygame.init()

WINDOW_WIDTH = pygame.display.Info().current_w
WINDOW_HEIGHT = pygame.display.Info().current_h

pygame.display.set_caption("Snake")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)

game = Game(window=window)
game.run()

pygame.quit()