import pygame
from copy import deepcopy
from math import ceil

class Snake():
    
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, size_case_grid):
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.size_case_grid = size_case_grid
        self.rect = pygame.Rect(0, 0, self.size_case_grid, self.size_case_grid)
        self.color = (255, 255, 255)
        self.velocity = [0, 0]
        self.max_slow_speed = 10
        self.slow_speed = self.max_slow_speed
        self.lenght = 1
        self.data = [self.rect]

    def move(self):
        if self.slow_speed == 0:
            self.rect.x += self.velocity[0]*self.size_case_grid
            self.rect.y += self.velocity[1]*self.size_case_grid

            # Téléportation du côté inverse des murs
            if self.rect.x < 0:
                self.rect.x = self.size_case_grid*(ceil(self.WINDOW_WIDTH/self.size_case_grid))
            elif self.rect.x >= self.size_case_grid*(ceil(self.WINDOW_WIDTH/self.size_case_grid)):
                self.rect.x = 0
            elif self.rect.y < 0:
                self.rect.y = self.size_case_grid*(ceil(self.WINDOW_HEIGHT/self.size_case_grid))
            elif self.rect.y >= self.size_case_grid*(ceil(self.WINDOW_HEIGHT/self.size_case_grid)):
                self.rect.y = 0

            # Historique des x dernière positions de la tête du serpent
            self.data.append(deepcopy(self.rect))
            if len(self.data) > self.lenght:
                self.data.pop(0)

            self.slow_speed = self.max_slow_speed

    def add_lenght(self):
        self.lenght += 1
    
    def init(self):
        self.lenght = 1
        self.data = [self.rect]