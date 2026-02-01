import random
import pygame
from pygame.locals import *

import constants
import enemy as Enemy

# Initialise screen
pygame.init()
# Borderless Fullscreen
screen = pygame.display.set_mode((1920, 1080),)
pygame.display.set_caption('xTyper')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
clock = pygame.time.Clock()

center = (screen.get_width()/2, screen.get_height()/2)



# Spawn Enemy Event
SPAWNENEMY = pygame.USEREVENT
pygame.time.set_timer(SPAWNENEMY, 2000)

def main():
    enemy_list = []
    while True:
        background.fill((255, 251, 241))
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                for enemy in enemy_list:
                    enemy.check_input(event.unicode)
                enemy_list = [enemy for enemy in enemy_list if enemy.alive]
            if event.type == SPAWNENEMY:
                spawn_enemy(enemy_list)


        for enemy in enemy_list:
            enemy.update_position()

        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(240)

def spawn_enemy(enemy_list):
    spawn = random.randint(0, 1)
    x_spawn_points = (0, screen.get_width())
    x_distance = screen.get_width() / 6
    y_spawn_points = (0, screen.get_height())
    y_distance = screen.get_height() / 6
    word = random.choice(constants.word_list)
    #Side Spawn
    if spawn == 0:
        e = Enemy.Enemy(word,
                        background,
                        x_spawn_points[random.randint(0,1)],
                        int(y_distance*random.randint(0,7)),
                        center)
        enemy_list.append(e)
    #Upper Spawn
    if spawn == 1:
        e = Enemy.Enemy(word,
                        background,
                        int(x_distance*random.randint(0,7)),
                        y_spawn_points[random.randint(0,1)],
                        center)
        enemy_list.append(e)


if __name__ == '__main__': main()