import pygame
from cryptography.fernet import Fernet
from ast import literal_eval
import cryptography.fernet

class Out_menu():

    def __init__(self, window):
        self.window = window
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = pygame.display.get_surface().get_size()
        self.running = True
        self.button_restart_rect = pygame.Rect(self.WINDOW_WIDTH/2-150, self.WINDOW_HEIGHT/2-150, 300, 100)
        self.button_quit_rect = pygame.Rect(self.WINDOW_WIDTH/2-150, self.WINDOW_HEIGHT/2+50, 300, 100)
        self.button_rect_color = (255, 22, 100)
        self.button_restart_color = (255, 22, 100)
        self.button_quit_color = (255, 22, 100)
        self.button_color_default = (255, 22, 100)
        self.button_color_hover = (255, 22, 150)
        self.police = pygame.font.SysFont("comicsansms", 50)
        self.button_restart = self.police.render("REJOUER", True, self.button_rect_color)
        self.button_quit = self.police.render("QUITTER", True, self.button_rect_color)
        self.value_returned = 0
        self.text_score = self.police.render('0', True, (255, 255, 255))
        self.text_max_score = self.police.render('0', True, (255, 255, 255))
        self.color_max_score = (255, 255, 255)
        f = open("key.key", "rb")
        self.key = f.read()
        f.close()
        try:
            self.fernet = Fernet(self.key)
        except ValueError:
            with open("key.key", "wb") as f:
                self.key = Fernet.generate_key()
                f.write(self.key)
            self.fernet = Fernet(self.key)
        self.score = 0
        self.max_score = 0

    def set_score(self, score):
        self.score = score
        if self.max_score < score:
            self.color_max_score = (0, 255, 0)
            data = {"max_score": score}
            encrypted = self.fernet.encrypt(str(data).encode("UTF-8"))
            f = open("data.json", "wb")
            f.write(encrypted)
            f.close()
        else:
            self.color_max_score = (255, 255, 255)
        self.get_score()

    def get_score(self):
        f = open("data.json", "rb")
        try:
            decrypted = str(self.fernet.decrypt(f.read().decode("UTF-8")).decode("UTF-8"))
        except cryptography.fernet.InvalidToken:
            with open("data.json", "wb") as f:
                f.write("".encode("UTF-8"))
                data = {"max_score": 0}
                encrypted = self.fernet.encrypt(str(data).encode("UTF-8"))
                f.write(encrypted)
            return 0
        f.close()
        decrypted = literal_eval(decrypted)
        self.max_score = decrypted["max_score"]

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.value_returned = -1
                    self.running = False
                elif event.key == pygame.K_RETURN:
                    self.value_returned = 0
                    self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_restart_rect.collidepoint(event.pos):
                    self.value_returned = 0
                    self.running = False
                elif self.button_quit_rect.collidepoint(event.pos):
                    self.value_returned = -1
                    self.running = False

    def styles(self):
        if self.button_restart_rect.collidepoint(pygame.mouse.get_pos()):
            self.button_restart_color = self.button_color_hover
        else:
            self.button_restart_color = self.button_color_default
        if self.button_quit_rect.collidepoint(pygame.mouse.get_pos()):
            self.button_quit_color = self.button_color_hover
        else:
            self.button_quit_color = self.button_color_default

    def display(self):
        self.window.fill((22, 22, 22))
        pygame.draw.rect(self.window, self.button_restart_color, self.button_restart_rect, 2, 20)
        pygame.draw.rect(self.window, self.button_quit_color, self.button_quit_rect, 2, 20)
        self.window.blit(self.button_restart, (self.WINDOW_WIDTH/2-self.button_restart.get_width()/2, self.WINDOW_HEIGHT/2-self.button_restart.get_height()/2-100))
        self.window.blit(self.button_quit, (self.WINDOW_WIDTH/2-self.button_quit.get_width()/2, self.WINDOW_HEIGHT/2-self.button_quit.get_height()/2+100))
        self.text_score = self.police.render(f"Score: {self.score}", True, (255, 255, 255))
        self.text_max_score = self.police.render(f"Votre meilleur score: {self.max_score}", True, self.color_max_score)
        self.window.blit(self.text_score, (self.WINDOW_WIDTH/2-self.text_score.get_width()/2, self.WINDOW_HEIGHT/2-self.text_score.get_height()-300))
        self.window.blit(self.text_max_score, (self.WINDOW_WIDTH/2-self.text_max_score.get_width()/2, self.WINDOW_HEIGHT/2-300))
        pygame.display.flip()


    def run(self):
        self.running = True
        while self.running:
            self.handling_events()
            self.styles()
            self.display()
        return self.value_returned