import pygame

class out_menu():
    
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

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.handling_events()
            self.styles()
            self.display()
        return self.value_returned