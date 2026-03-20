import pygame
import random


class Background:
    def __init__(self, tileset_path="assets/Background/Dungeon_24x24.png", tile_size=48):
        self.tile_size = tile_size

        self.tileset = pygame.image.load(tileset_path).convert_alpha()


        self.tile_coords = [
            pygame.Rect(288, 0, 24, 24),
            pygame.Rect(312, 0, 24, 24),
            pygame.Rect(288, 24, 24, 24),
            pygame.Rect(312, 24, 24, 24),
            pygame.Rect(288, 48, 24, 24),
            pygame.Rect(312, 48, 24, 24)
        ]


        self.floor_tiles = []
        for rect in self.tile_coords:
            subsurface = self.tileset.subsurface(rect)
            scaled_tile = pygame.transform.scale(subsurface, (self.tile_size, self.tile_size))
            self.floor_tiles.append(scaled_tile)

    def get_background(self, screen_width, screen_height):
        bg_surface = pygame.Surface((screen_width, screen_height))

        weights = [5, 5, 15, 15, 30, 30]

        for y in range(0, screen_height, self.tile_size):
            for x in range(0, screen_width, self.tile_size):
                chosen_tile = random.choices(self.floor_tiles, weights=weights)[0]
                bg_surface.blit(chosen_tile, (x, y))

        return bg_surface