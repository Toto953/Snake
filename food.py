import pygame

class Food(pygame.sprite.Sprite):

    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, size_case_grid):
        super().__init__()
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.size_case_grid = size_case_grid
        self.color = (32, 32, 255)
        self.rect = pygame.Rect(0, 0, self.size_case_grid, self.size_case_grid)
        self.list_of_positionsX = []
        self.list_of_positionsY = []
        for x in range(WINDOW_WIDTH):
            if x % self.size_case_grid == 0:
                self.list_of_positionsX.append(x)
        for y in range(WINDOW_HEIGHT):
            if y % self.size_case_grid == 0:
                self.list_of_positionsY.append(y)

    def spawn(self, x, y):
        self.rect.x = x
        self.rect.y = y