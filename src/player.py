import pygame
import constants

class Player:
    def __init__(self, surface):
        self.pos_x = surface.get_width()/2
        self.pos_y = surface.get_height()/2
        self.hitbox_radius = constants.PLAYER_RADIUS
        self.surface = surface

        self.internal_timer = 0
        self.frame = 0
        self.state = "Idle"
        self.path_sprite = "assets/Player/"
        self.frame_width = 48
        self.frame_height = 64

    def draw(self):


        image = pygame.image.load(self.path_sprite + self.state + ".png").convert_alpha()
        current_frame = pygame.transform.scale_by(
            image.subsurface(self.frame_width * self.frame, 0, self.frame_width, self.frame_height), 4)
        current_frame_rect = current_frame.get_rect()
        current_frame_rect.center = (self.pos_x, self.pos_y)
        self.surface.blit(current_frame, current_frame_rect)
    def update(self, delta_time):
        self.internal_timer += delta_time * 10
        self.frame = int(self.internal_timer)
        if self.frame >= 8:
            self.internal_timer = 0
            self.frame = 0
            self.state = "Idle"

    def shoot(self, angle):
        self.state = self.calculate_state_from_angle()

    def calculate_state_from_angle(self, angle):
        shifted_angle = (angle + 22.5) % 360
        index = int(shifted_angle // 45)
        self.internal_timer = 0
        self.frame = 0

        state = {
            0: "Shooting_Right",
            1: "Shooting_Down_Right",
            2: "Shooting_Down",
            3: "Shooting_Down_Left",
            4: "Shooting_Left",
            5: "Shooting_Up_Left",
            6: "Shooting_Up",
            7: "Shooting_Up_Right"
        }
        self.state = state[index]

