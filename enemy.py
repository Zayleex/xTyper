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
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.alive = True
        self.create_object(self.surface, self.pos_x, self.pos_y)


    def create_object(self, surface: pygame.Surface, pos_x: int, pos_y: int):
        circle = pygame.draw.circle(surface=self.surface,
                                    color=const.CIRCLE_COLOR,
                                    center=(pos_x, pos_y),
                                    radius=const.CIRCLE_RADIUS)
        pos_text = circle.topleft

        if self.letter_pos == 0:
            text_unwritten = const.FONT.render(self.word, 0, const.TEXT_UWWRITTEN)
            surface.blit(text_unwritten, (pos_text[0], pos_text[1] - 20))
        else:
            print(self.word[0:self.letter_pos])
            print(self.word[self.letter_pos:self.word_length-1])
            text_written = const.FONT.render(self.word[0:self.letter_pos], 0, const.TEXT_WRITTEN)
            text_unwritten = const.FONT.render(self.word[self.letter_pos:self.word_length], 0, const.TEXT_UWWRITTEN)
            pos_text_unwritten = surface.blit(text_written, (pos_text[0], pos_text[1] - 20)).topright
            surface.blit(text_unwritten, pos_text_unwritten)


    def update_position(self):
        self.pos_x += 0.1
        self.pos_y += 0.1
        self.create_object(self.surface, self.pos_x, self.pos_y)


    def check_input(self, letter: str):
        if self.word[self.letter_pos] == letter:
            self.letter_pos += 1
        else:
            self.letter_pos = 0
        self.check_alive()


    def check_alive(self):
        if self.word_length == self.letter_pos:
            self.alive = False
