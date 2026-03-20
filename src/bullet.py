import pygame

import constants

class Bullet:
    def __init__(self, surface, letter, target, version):
        self.surface = surface
        self.letter = letter
        self.pos_x = surface.get_width()/2
        self.pos_y = surface.get_height()/2
        self.version = version
        self.target = target
        self.alive = True
        self.vector = pygame.math.Vector2.normalize(pygame.math.Vector2(target.pos_x - self.pos_x, target.pos_y - self.pos_y))
        self.hitbox_radius = constants.BULLET_RADIUS

        self.internal_timer = 0
        self.frame = 0
        self.sprite_sheet = pygame.transform.scale_by(pygame.image.load("assets/Bullet/Idle.png"), 2)
        self.frame_width = 16
        self.frame_height = 16

    def draw(self):
        #pygame.draw.circle(self.surface, (255, 107, 107), (self.pos_x, self.pos_y), constants.BULLET_RADIUS)
        current_frame = self.sprite_sheet.subsurface(0 + self.frame_width * 2 * self.frame, 0, self.frame_width * 2,
                                                     self.frame_height * 2)
        current_frame_rect = current_frame.get_rect(center=(self.pos_x, self.pos_y))
        self.surface.blit(current_frame, current_frame_rect)

        text = constants.FONT_BULLET.render(self.letter, True, "black")
        text_rect = text.get_rect()
        text_rect.center = (self.pos_x, self.pos_y)
        self.surface.blit(text, text_rect)


    def update(self, delta_time):
        self.pos_x += constants.GAME_SPEED * delta_time * self.vector[0] * 10
        self.pos_y += constants.GAME_SPEED * delta_time * self.vector[1] * 10

        if self.frame >= 3:
            self.frame = 3
            return
        self.internal_timer += delta_time * 10
        self.frame = int(self.internal_timer)

