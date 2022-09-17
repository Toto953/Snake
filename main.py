import pygame
from game import Game

pygame.init()

WINDOW_WIDTH = pygame.display.Info().current_w
WINDOW_HEIGHT = pygame.display.Info().current_h

pygame.display.set_caption("Snake")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)

game = Game(window=window)
game.run()

pygame.quit()