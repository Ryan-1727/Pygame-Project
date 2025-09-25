import pygame
from utils import load_map, load_frames
import os


class TileMap:
    CONFIG = {
        # brick
        'B': {"file": "town_tiles.png", "frame_w": 16, "frame_h": 16, "start_x": 0, "start_y": 0,
              "num_frames": 1, "scale": 1},
        # grass
        'G': {"file": "grass_tile.png", "frame_w": 16, "frame_h": 16, "start_x": 0, "start_y": 0,
              "num_frames": 1, "scale": 1},
        # path
        'P': {"file": "path_tile.png", "frame_w": 16, "frame_h": 16, "start_x": 0, "start_y": 0,
              "num_frames": 1, "scale": 1},
        # water
        'W': {"file": "water_tile.png", "frame_w": 16, "frame_h": 16, "start_x": 0, "start_y": 0,
              "num_frames": 1, "scale": 1},
        'L': {"file": "path_diagonal_left.png", "frame_w": 16, "frame_h": 16, "start_x": 0, "start_y": 0,
              "num_frames": 1, "scale": 1},
        'R': {"file": "path_diagonal_right.png", "frame_w": 16, "frame_h": 16, "start_x": 0, "start_y": 0,
              "num_frames": 1, "scale": 1},
        'D': {"file": "dirt_tile.png", "frame_w": 16, "frame_h": 16, "start_x": 0, "start_y": 0,
              "num_frames": 1, "scale": 1},
    }

    def __init__(self, filename, tile_size=16):
        self.map_grid = load_map(filename)
        self.tile_size = tile_size
        self.tiles = {}

        # preload all tiles into memory
        for tile_id, cfg in self.CONFIG.items():
            sheet = pygame.image.load(os.path.join('assets', 'images', 'tiles', cfg["file"])).convert_alpha()
            frames = load_frames(
                sheet,
                cfg["frame_w"],
                cfg["frame_h"],
                cfg["start_x"],
                cfg["start_y"],
                cfg["num_frames"],
                cfg["scale"],
            )
            self.tiles[tile_id] = frames[0]

    def draw(self, surface, camera):
        for row_index, row in enumerate(self.map_grid):
            for col_index, tile_id in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size
                tile_image = self.tiles.get(tile_id, self.tiles['G'])
                surface.blit(tile_image, (x + camera.offset.x, y + camera.offset.y))

    def get_map_size(self):
        map_width = len(self.map_grid[0]) * self.tile_size
        map_height = len(self.map_grid) * self.tile_size
        return map_width, map_height

