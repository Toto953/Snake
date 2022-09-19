import pygame
from food import Food
from grid import Grid
from main_menu import Main_menu
from out_menu import Out_menu
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
        self.food.spawn(choice(self.food.list_of_positionsX), choice(self.food.list_of_positionsY))
        self.running = True
        self.in_main_menu = True
        self.in_game = False
        self.in_out_menu = False
        self.main_menu = Main_menu(self.window)
        self.out_menu = Out_menu(self.window)
        self.score = 1
        self.score_police = pygame.font.SysFont("comicsansms", 32, True)
        self.text_score = self.score_police.render(f"score: {self.score}", True, (255, 255, 255))

    def init(self):
        self.score = 1
        self.text_score = self.score_police.render(f"score: {self.score}", True, (255, 255, 255))

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
                self.food.rect.x = choice(self.food.list_of_positionsX)
                self.food.rect.y = choice(self.food.list_of_positionsY)
                for i in self.snake.data:
                    if i[0] == self.food.rect.x and i[1] == self.food.rect.y:
                        s = False
                        break
                if s == True:
                    good = True
            self.food.spawn(self.food.rect.x, self.food.rect.y)
            self.snake.add_lenght()
            self.score+=1
            self.text_score = self.score_police.render(f"score: {self.score}", True, (255, 255, 255))

        # Si le serpent se mord lui-même la queue
        if self.snake.data[-1] in self.snake.data[:-1] and self.snake.data[-1] in self.snake.data[:-1]:
            self.out_menu.get_score()
            self.out_menu.set_score(self.score)
            self.init()
            self.snake.init()
            self.in_game = False
            self.in_out_menu = True


    # Affichage
    def display(self):
        self.window.fill((32, 32, 32))
        for i in range(self.snake.lenght):
            pygame.draw.rect(self.window, self.snake.color, self.snake.data[i-1])
        self.grid.draw()
        pygame.draw.rect(self.window, self.food.color, self.food.rect, border_radius=int(self.size_case_grid/2))
        self.window.blit(self.text_score, (50, 50))
        pygame.display.flip()

    # Boucle du programme
    def run(self):
        while self.running:
            if self.in_main_menu:
                if self.main_menu.run() == 0:
                    self.in_main_menu = False
                    self.in_game = True
                elif self.main_menu.run() == -1:
                    self.running = False
            elif self.in_game:
                self.clock.tick(240)
                self.handling_events()
                self.update()
                self.display()
            elif self.in_out_menu:
                if self.out_menu.run() == 0:
                    self.in_out_menu = False
                    self.in_game = True
                elif self.out_menu.run() == -1:
                    self.running = False