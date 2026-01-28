import random
import pygame
from pygame.locals import *

import enemy as ene

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('xTyper')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
clock = pygame.time.Clock()



def main():
    enemy_list = []
    temp_list = []
    while True:
        e = ene.Enemy("Hallo", background, random.randint(0, 1000), random.randint(0, 1000))
        enemy_list.append(e)
        background.fill((250, 250, 250))

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                for enemy in enemy_list:
                    print(event.unicode)
                    enemy.check_input(event.unicode)
                    if enemy.alive:
                        temp_list.append(enemy)
                enemy_list = temp_list
                temp_list = []
        for enemy in enemy_list:
            enemy.update_position()

        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(240)


if __name__ == '__main__': main()