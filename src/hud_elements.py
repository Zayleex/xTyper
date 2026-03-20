import pygame
import constants

class Timer:
    def __init__(self, surface):
        self.seconds = 0
        self.surface = surface

    def draw(self):
        text = self.calculate_time()
        points = constants.FONT_SCORE.render(text, True, "white")
        score_rect = points.get_rect()
        score_rect.topleft = (0, 0)
        self.surface.blit(points, score_rect)

    def calculate_time(self):
        total_seconds = self.seconds

        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600

        minutes = remaining_seconds // 60

        seconds = remaining_seconds % 60

        return f"{hours:02}:{minutes:02}:{seconds:02}"


    def get_time(self, time):
        self.seconds = time

class HealthBar:
    def __init__(self, surface):
        self.health = 100
        self.surface = surface
        self.screen_width = surface.get_width()
        self.screen_height = surface.get_height()

        rect_health_border = pygame.Rect(0, 0, 500, 30)
        rect_health_border.midtop = (self.screen_width/2, 13)
        self.rect_health_border = rect_health_border

    def decrease_health(self):
        self.health -= 10

    def draw(self):
        rect_health = pygame.Rect(0, 0, (self.health/10) * 50 , 30)
        rect_health.topleft = self.rect_health_border.topleft
        pygame.draw.rect(self.surface, "red", rect_health)
        pygame.draw.rect(self.surface, "black", self.rect_health_border, 3)


class Score:
    def __init__(self, surface):
        self.points = 0
        self.surface = surface
        self.screen_width = surface.get_width()
        self.multiplier = 1

    def draw(self):
        prefix_length = constants.MAX_SCORE_LENGTH - len(str(self.points))
        prefix = "0" * prefix_length
        score = prefix + str(self.points)
        points = constants.FONT_SCORE.render(score, True, "white")
        score_rect = points.get_rect(topright=(self.screen_width, 0))
        self.surface.blit(points, score_rect)

        multiplier = constants.FONT_SCORE.render(f"x{self.multiplier}", True, "white")
        multiplier_rect = multiplier.get_rect(center=(score_rect.centerx, score_rect.centery + 50))
        self.surface.blit(multiplier, multiplier_rect)

    def add_points(self, points):
        self.points += points * 100 * self.multiplier

    def add_multiplier(self):
        self.multiplier += 1

    def reset_multiplier(self):
        self.multiplier = 1


