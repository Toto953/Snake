import pygame
from copy import deepcopy

class Snake():
    
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, size_case_grid):
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.size_case_grid = size_case_grid
        self.rect = pygame.Rect(320, 320, self.size_case_grid-1, self.size_case_grid-1)
        self.color = (255, 255, 255)
        self.velocity = [0, 0]
        self.max_slow_speed = 10
        self.slow_speed = self.max_slow_speed
        self.lenght = 1
        self.data = [pygame.Rect(320, 320, 63, 63)]

    def move(self, window):
        if self.slow_speed == 0:

            if self.lenght < 24:
                self.lenght+=1

            self.rect.x += self.velocity[0]*self.size_case_grid
            self.rect.y += self.velocity[1]*self.size_case_grid

            self.data.append(deepcopy(self.rect))

            if len(self.data) > self.lenght:
                self.data.pop(0)

            self.slow_speed = self.max_slow_speed
