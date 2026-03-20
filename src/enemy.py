import constants
import pygame

class Enemy:
    def __init__(self, word, surface, pos_x, pos_y):

        self.pos_x, self.pos_y = pos_x, pos_y
        self.hitbox_radius = constants.ENEMY_RADIUS
        self.screen_width, self.screen_height = surface.get_width(), surface.get_height()
        self.surface = surface
        self.word = word
        self.hp = len(word)
        self.letter_pos = 0
        self.alive = True
        self.direction_vector = pygame.math.Vector2.normalize(pygame.math.Vector2(self.screen_width / 2 - pos_x, self.screen_height / 2 - pos_y))

        self.version = 0
        self.internal_timer = 0
        self.frame = 0
        self.sprite_sheet =  pygame.transform.scale_by(pygame.image.load("assets/Enemy/Walk.png"), 3.0)
        self.frame_width = 96
        self.frame_height = 96

    def draw(self):
        # Get current Image
        current_frame = self.sprite_sheet.subsurface(0 + self.frame_width * 3 *self.frame, 0, self.frame_width*3, self.frame_height*3)
        current_frame_rect = current_frame.get_rect(center=(self.pos_x, self.pos_y))
        self.surface.blit(current_frame, current_frame_rect)

        # Draw unwritten Text
        if self.letter_pos >= len(self.word):
            return
        text_unwritten = constants.FONT.render(self.word, True, constants.TEXT_UWWRITTEN)
        text_unwritten_rect = text_unwritten.get_rect(center=(self.pos_x, self.pos_y-constants.ENEMY_DISTANCE_TEXT))
        self.surface.blit(text_unwritten, text_unwritten_rect)

        #Draw written Text over unwritten Text
        if self.letter_pos > 0:
            text_written = constants.FONT.render(self.word[0:self.letter_pos], True, constants.TEXT_WRITTEN)
            text_written_rect = text_written.get_rect(left=text_unwritten_rect.left, centery=text_unwritten_rect.centery)
            self.surface.blit(text_written, text_written_rect)

    def update(self, delta_time):
        """Update position"""
        self.pos_x += constants.GAME_SPEED * delta_time * self.direction_vector[0]
        self.pos_y += constants.GAME_SPEED * delta_time * self.direction_vector[1]

        #Internal Calculation for frame management
        self.internal_timer += delta_time  * 10
        self.frame = int(self.internal_timer)
        if self.frame >= 8:
            self.internal_timer = 0
            self.frame = 0

    def take_damage(self):
        self.hp -= 1
        if self.hp <= 0:
            self.alive = False

    def check_input(self, letter):
        #When Word already done, dont check anymore
        if self.letter_pos >= len(self.word):
            return False
        #If letter matches
        if self.word[self.letter_pos] == letter:
            self.letter_pos += 1
            return True
        #If letter doesnt match
        else:
            self.letter_pos = 0
            self.version += 1
            self.hp = len(self.word)
            return False
