import pygame
from utils import load_frames


class StaticEntity(pygame.sprite.Sprite):
    CONFIG = {
        0: {"file": "campfire.png", "frame_w": 64, "frame_h": 64, "start_x": 0, "start_y": 0,
            'num_frames': 5, 'scale': 1},
        1: {"file": "pathAndObjects.png", "frame_w": 128, "frame_h": 96, "start_x": 384, "start_y": 0,
            'num_frames': 1, 'scale': 0.5},
        2: {"file": "pathAndObjects.png",  "frame_w": 128, "frame_h": 64,   "start_x": 384, "start_y": 280,
            'num_frames': 1, 'scale': 0.5},
        3: {"file": "evergreen.png", "frame_w": 48, "frame_h": 75, "start_x": 0, "start_y": 0,
            'num_frames': 1, 'scale': 1},
    }

    def __init__(self, pos, entity_type=0, frame_speed=0.1):
        super().__init__()
        self.frame_speed = frame_speed
        self.entity_type = entity_type

        # Pull config for this entity
        cfg = self.CONFIG.get(entity_type, self.CONFIG[0])
        sheet = pygame.image.load(cfg["file"]).convert_alpha()

        # Load frames with custom parameters
        self.frames = load_frames(sheet, cfg["frame_w"], cfg["frame_h"], cfg["start_x"], cfg["start_y"],
                                  cfg['num_frames'], cfg['scale'])

        # Default state
        self.animated = cfg['num_frames'] > 1

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.time_accumulator = 0

    def update(self, dt, keys):
        # Animate frames
        if self.animated:
            self.time_accumulator += dt
            if self.time_accumulator >= self.frame_speed:
                self.time_accumulator -= self.frame_speed
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.image = self.frames[self.frame_index]
