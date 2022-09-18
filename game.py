import pygame
from food import Food
from grid import Grid
from snake import Snake
from random import choice

class Game():

    def __init__(self, window):
        self.window = window
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = pygame.display.get_surface().get_size()
        self.size_case_grid = int(self.WINDOW_WIDTH/30)
        self.snake = Snake(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.size_case_grid)
        self.grid = Grid(self.window, self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.size_case_grid)
        self.food = Food(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.size_case_grid)
        self.clock = pygame.time.Clock()
        self.food.spawn(choice(self.food.positionsX), choice(self.food.positionsY))
        self.running = True

    # Evenements de l'utilisateur
    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                # Contrôle du serpent
                if event.key == pygame.K_LEFT:
                    if self.snake.velocity[0] != 1:
                        self.snake.velocity[0] = -1
                    self.snake.velocity[1] = 0
                elif event.key == pygame.K_RIGHT:
                    if self.snake.velocity[0] != -1:
                        self.snake.velocity[0] = 1
                    self.snake.velocity[1] = 0
                elif event.key == pygame.K_UP:
                    if self.snake.velocity[1] != 1:
                        self.snake.velocity[1] = -1
                    self.snake.velocity[0] = 0
                elif event.key == pygame.K_DOWN:
                    if self.snake.velocity[1] != -1:
                        self.snake.velocity[1] = 1
                    self.snake.velocity[0] = 0

    # Logique du jeu
    def update(self):
        self.snake.slow_speed -= 1
        self.snake.move()

        # Regénération de la pomme lorsque le serpent la mange
        if self.food.rect.colliderect(self.snake.data[-1]):
            good = False
            while not good:
                s = True
                self.food.rect.x = choice(self.food.positionsX)
                self.food.rect.y = choice(self.food.positionsY)
                for i in self.snake.data:
                    if i[0] == self.food.rect.x and i[1] == self.food.rect.y:
                        s = False
                        break
                if s == True:
                    good = True
            self.food.spawn(self.food.rect.x, self.food.rect.y)
            self.snake.add_lenght()

        # Si le serpent se mord lui-même la queue
        if self.snake.data[-1] in self.snake.data[:-1] and self.snake.data[-1] in self.snake.data[:-1]:
            self.running = False


    # Affichage
    def display(self):
        self.window.fill((32, 32, 32))
        for i in range(self.snake.lenght):
            pygame.draw.rect(self.window, self.snake.color, self.snake.data[i-1])
        self.grid.draw(self.window, self.size_case_grid)
        pygame.draw.rect(self.window, self.food.color, self.food.rect, border_radius=int(self.size_case_grid/2))
        pygame.display.flip()

    # Boucle du programme
    def run(self):
        while self.running:
            self.clock.tick(240)
            self.handling_events()
            self.update()
            self.display()