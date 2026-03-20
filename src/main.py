import pygame
from game import Game
from start_menu import Start_Menu

pygame.init()

screen_layer = pygame.display.set_mode((0, 0), pygame.NOFRAME)
pygame.display.set_caption('xTyper')
clock = pygame.time.Clock()


def main():
    game = Game(screen_layer)
    menu = Start_Menu(screen_layer)
    current_state = "MENU"
    running = True

    while running:
        events = pygame.event.get()
        if current_state == "MENU":
            current_state = menu.run(events)
        if current_state == "GAME":
            current_state = game.run(events)
        if current_state == "QUIT":
            running = False
        pygame.display.flip()
        game.dt = clock.tick(240) / 1000.0
    pygame.quit()

if __name__ == '__main__':
    main()