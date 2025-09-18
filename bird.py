import pygame
from utils import load_frames
from animated_sprite import AnimatedSprite


class Bird(AnimatedSprite):
    def __init__(self, pos, speed, x_range, bird_type=0):
        self.bird_type = bird_type
        images = {0: 'bluejay.png', 1: 'whitebird.png', 2: 'redbird.png'}
        image = images.get(self.bird_type, 'bluejay.png')  # default to bluejay

        fly_left = load_frames(pygame.image.load(image).convert_alpha(), 32, 32, 0, 0, 3, 1)
        fly_right = [pygame.transform.flip(f, True, False) for f in fly_left]
        super().__init__(pos, speed, x_range, frames_right=fly_right, frames_left=fly_left)
