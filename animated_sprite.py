import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, pos, speed, x_range, frames_right, frames_left=None, frame_speed=0.1):
        super().__init__()
        self.frames_right = frames_right
        self.frames_left = frames_left if frames_left else [pygame.transform.flip(f, True, False) for f in frames_right]
        self.current_frames = self.frames_right

        self.frame_index = 0
        self.image = self.current_frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        self.speed = speed
        self.x_range = x_range
        self.moving_right = True
        self.frame_speed = frame_speed
        self.time_accumulator = 0

    def update(self, dt, keys):
        # Automatic horizontal movement
        if self.moving_right:
            self.rect.x += int(self.speed * dt)
            self.current_frames = self.frames_right
            if self.rect.right >= self.x_range[1]:
                self.moving_right = False
        else:
            self.rect.x -= int(self.speed * dt)
            self.current_frames = self.frames_left
            if self.rect.left <= self.x_range[0]:
                self.moving_right = True

        # Animate frames
        self.time_accumulator += dt
        if self.time_accumulator >= self.frame_speed:
            self.time_accumulator -= self.frame_speed
            self.frame_index = (self.frame_index + 1) % len(self.current_frames)
            self.image = self.current_frames[self.frame_index]
