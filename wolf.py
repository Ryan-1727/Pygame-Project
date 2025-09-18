import pygame
from utils import load_frames
from animated_sprite import AnimatedSprite


class Wolf(AnimatedSprite):
    def __init__(self, pos, speed, x_range):
        walk_right = load_frames(pygame.image.load('wolfsheet6.png').convert_alpha(), 64, 32, 320, 96, 4, 1)
        super().__init__(pos, speed, x_range, frames_right=walk_right)
