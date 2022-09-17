import pygame
from grid import Grid
from snake import Snake

class Game():

    def __init__(self, window):
        self.window = window
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = pygame.display.get_surface().get_size()
        self.size_case_grid = int(self.WINDOW_WIDTH/30)
        self.snake = Snake(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.size_case_grid)
        self.grid = Grid(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.running = True
        self.clock = pygame.time.Clock()

    # Evenements de l'utilisateur
    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                
                if event.key == pygame.K_LEFT:
                    self.snake.velocity[0] = -1
                    self.snake.velocity[1] = 0
                elif event.key == pygame.K_RIGHT:
                    self.snake.velocity[0] = 1
                    self.snake.velocity[1] = 0
                elif event.key == pygame.K_UP:
                    self.snake.velocity[1] = -1
                    self.snake.velocity[0] = 0
                elif event.key == pygame.K_DOWN:
                    self.snake.velocity[1] = 1
                    self.snake.velocity[0] = 0

    # Logique du jeu
    def update(self):
        self.snake.move(self.window)
        self.snake.slow_speed -= 1

    # Affichage
    def display(self):
        self.window.fill((32, 32, 32))
        for i in range(self.snake.lenght):
            pygame.draw.rect(self.window, self.snake.color, self.snake.data[i])
        self.grid.draw(self.window, self.size_case_grid)
        pygame.display.flip()

    # Boucle du programme
    def run(self):
        while self.running:
            self.clock.tick(144)
            self.handling_events()
            self.update()
            self.display()