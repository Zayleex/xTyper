from pygame.sprite import Sprite

import constants as const
import pygame
from pygame.draw import circle



class Enemy:
    def __init__(self, word: str, surface: pygame.Surface, pos_x: int, pos_y: int):
        self.word = word
        self.word_length = len(word)
        self.letter_pos = 0
        self.surface = surface

        drawn_circle = pygame.draw.circle(surface=self.surface,
                                          color=const.CIRCLE_COLOR,
                                          center=(pos_x, pos_y),
                                          radius=const.CIRCLE_RADIUS)
        print(drawn_circle.topleft)
        rendered_text = const.FONT.render("Test", (100, 100, 100), (0, 0, 0))
        surface.blit(rendered_text, (90, 70))


    def check_input(self, letter: str):
        if self.word[self.letter_pos] == letter:
            self.letter_pos += 1
