import pygame


class Button:
    def __init__(self, text, x_pos, y_pos, width, height, surface):
        self.text = text
        self.font = pygame.font.SysFont("Helvetica", 32)
        self.surface = surface
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x_pos, y_pos)

    def draw(self, mouse_pos):
        is_hovered = self.rect.collidepoint(mouse_pos)


        cream_white = (238, 232, 213)

        dark_slate = (45, 40, 55)

        text_color = dark_slate if is_hovered else cream_white

        if is_hovered:
            pygame.draw.rect(self.surface, cream_white, self.rect, border_radius=15)
        else:
            pygame.draw.rect(self.surface, cream_white, self.rect, border_radius=15, width=3)

        # Text rendern und platzieren
        text_surf = self.font.render(self.text, True, text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        self.surface.blit(text_surf, text_rect)

    def is_clicked(self, event, mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(mouse_pos):
                return True
        return False


class HeaderText:
    def __init__(self, text, x, y, surface, color=(238, 232, 213) ):
        self.text = text
        self.font = pygame.font.SysFont("Helvetica", 120, bold=True)
        self.color = color
        self.surf = self.font.render(self.text, True, self.color)
        self.rect = self.surf.get_rect(center=(x, y))
        self.surface = surface

    def draw(self):
        self.surface.blit(self.surf, self.rect)