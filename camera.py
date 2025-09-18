import pygame


class Camera:
    def __init__(self, screen_width, screen_height, map_width, map_height):
        self.offset = pygame.Vector2(0, 0)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_width = map_width
        self.map_height = map_height
        self.screen_center_x = screen_width // 2
        self.screen_center_y = screen_height // 2

        # Calculate the boundaries for the camera's offset
        self.camera_bounds_x = map_width - screen_width
        self.camera_bounds_y = map_height - screen_height

    def update(self, target):
        # The camera's offset is calculated to keep the target (player)
        # at the center of the screen
        self.offset.x = self.screen_center_x - target.rect.centerx
        self.offset.y = self.screen_center_y - target.rect.centery

        # Clamp the camera's offset to prevent it from going past map edges
        self.clamp_camera()

    def clamp_camera(self):
        # Clamp X
        if self.offset.x > 0:
            self.offset.x = 0
        elif self.offset.x < -self.camera_bounds_x:
            self.offset.x = -self.camera_bounds_x

        # Clamp Y
        if self.offset.y > 0:
            self.offset.y = 0
        elif self.offset.y < -self.camera_bounds_y:
            self.offset.y = -self.camera_bounds_y

    def apply(self, rect):
        return rect.move(self.offset)