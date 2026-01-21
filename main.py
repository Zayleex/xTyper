import pygame
from pygame.locals import *
import enemy

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('xTyper')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
clock = pygame.time.Clock()
e = enemy.Enemy("Hallo", background, 100, 100)

def main():
    # Event loop
    while True:
        background.fill((250, 250, 250))
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                e.check_input(event.unicode)
        e.update_position()
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(240)


if __name__ == '__main__': main()