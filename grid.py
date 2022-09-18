import pygame

class Grid():

    def __init__(self, window, WINDOW_WIDTH, WINDOW_HEIGHT, size_case_grid):
        self.window = window
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.size_case_grid = size_case_grid
        self.color = (0, 0, 0)
        self.width = 1

    def draw(self):
        for x in range(0, self.WINDOW_WIDTH, self.size_case_grid):
            pygame.draw.line(self.window,
                            self.color,
                            [x, 0],
                            [x, self.WINDOW_HEIGHT],
                            self.width)
        for y in range(0, self.WINDOW_HEIGHT, self.size_case_grid):
            pygame.draw.line(self.window,
                            self.color,
                            [0, y],
                            [self.WINDOW_WIDTH, y],
                            self.width)