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
background.fill((250, 250, 250))
enemy.Enemy("Hello", background, 100, 100)

def main():
    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()