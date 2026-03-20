import pygame
from background import Background
from ui_elements import HeaderText
from ui_elements import Button



class Start_Menu:
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()


        self.background = Background().get_background(self.width, self.height)


        self.title = HeaderText("xTyper", self.width // 2, self.height // 4, screen)


        self.start_button = Button("START GAME", self.width // 2, self.height // 2, 300, 70, screen)


        self.quit_button = Button("QUIT", self.width // 2, (self.height // 2) + 100, 300, 70, screen)

    def run(self, events):
        mouse_pos = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.QUIT:
                return "QUIT"


            if self.start_button.is_clicked(event, mouse_pos):
                return "GAME"

            if self.quit_button.is_clicked(event, mouse_pos):
                return "QUIT"

        self.draw(mouse_pos)
        return "MENU"

    def draw(self, mouse_pos):

        self.screen.blit(self.background, (0, 0))


        self.title.draw()
        self.start_button.draw(mouse_pos)
        self.quit_button.draw(mouse_pos)