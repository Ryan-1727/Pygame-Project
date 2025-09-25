import pygame
import random


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, pos, speed, x_bounds, frames_right, y_bounds=(0,0), movement_type="horizontal",
                 frames_left=None, frame_speed=0.1):
        super().__init__()
        self.frames_right = frames_right
        self.frames_left = frames_left if frames_left else [pygame.transform.flip(f, True, False) for f in frames_right]
        self.current_frames = self.frames_right
        self.movement_type = movement_type

        self.frame_index = 0
        self.image = self.current_frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        self.speed = speed
        self.moving_right = True
        self.moving_down = True
        self.frame_speed = frame_speed
        self.time_accumulator = 0

        # Variables for Horizontal Movement
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds

        # Variables for Stochastic Movement
        self.dest_x = self.rect.x
        self.dest_y = self.rect.y

    def update(self, dt, keys):

        # Automatic horizontal movement
        if self.movement_type == 'horizontal':
            if self.moving_right:
                self.rect.x += int(self.speed * dt)
                self.current_frames = self.frames_right
                if self.rect.right >= self.x_bounds[1]:
                    self.moving_right = False
            else:
                self.rect.x -= int(self.speed * dt)
                self.current_frames = self.frames_left
                if self.rect.left <= self.x_bounds[0]:
                    self.moving_right = True
        # Random movement
        else:
            if abs(self.rect.x - self.dest_x) < 5 and abs(self.rect.y - self.dest_y) < 5:
                self.dest_x = random.randint(self.x_bounds[0], self.x_bounds[1])
                self.dest_y = random.randint(self.y_bounds[0], self.y_bounds[1])

            # Calculate the distance to the destination
            dx = self.dest_x - self.rect.x
            dy = self.dest_y - self.rect.y

            # Normalize the vector to ensure consistent speed
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance > 0:
                dx /= distance
                dy /= distance

            # Update the sprite's position
            self.rect.x += int(dx * self.speed * dt)
            self.rect.y += int(dy * self.speed * dt)

            # Decide on animation frames based on horizontal direction
            if dx > 0:
                self.current_frames = self.frames_right
            else:
                self.current_frames = self.frames_left


        # Animate frames
        self.time_accumulator += dt
        if self.time_accumulator >= self.frame_speed:
            self.time_accumulator -= self.frame_speed
            self.frame_index = (self.frame_index + 1) % len(self.current_frames)
            self.image = self.current_frames[self.frame_index]
