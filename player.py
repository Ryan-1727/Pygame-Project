import pygame
from utils import load_frames


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, bounds):
        super().__init__()

        # --- Load animations ---
        player_image = pygame.image.load('Old hero.png').convert()
        player_image.set_colorkey((157, 142, 135))
        self.walk_right = load_frames(player_image, 16, 16, 16, 32, 4, 2)
        self.walk_left = [pygame.transform.flip(f, True, False) for f in self.walk_right]
        self.action_right = load_frames(player_image, 16, 16, 16, 80, 3, 2)
        self.action_left = [pygame.transform.flip(f, True, False) for f in self.action_right]
        self.idle_right = load_frames(player_image, 16, 16, 16, 16, 4, 2)
        self.idle_left = [pygame.transform.flip(f, True, False) for f in self.idle_right]

        # --- Initial state ---
        self.current_frames = self.idle_right
        self.frame_index = 0
        self.image = self.current_frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.bounds = pygame.Rect(bounds)

        # Movement + animation state
        self.speed = 200
        self.direction = "right"
        self.is_moving = False
        self.is_action = False
        self.action_done = True
        self.time_accumulator = 0  # We will use this to control the animation speed

        # Add frame speed attributes for different animations
        self.walk_frame_speed = 0.1
        self.idle_frame_speed = 0.2  # This is the value you will adjust
        self.current_frame_speed = self.idle_frame_speed

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.action_done:
                self.is_action = True
                self.action_done = False
                self.frame_index = 0

    def update(self, dt, keys):
        # Update action animation speed
        if self.is_action:
            self.current_frames = self.action_left if self.direction == "left" else self.action_right
            self.time_accumulator += dt
            if self.time_accumulator >= 0.1:  # Action speed is fixed
                self.time_accumulator = 0
                self.frame_index += 1
                if self.frame_index >= len(self.current_frames):
                    self.is_action = False
                    self.action_done = True
                    self.frame_index = 0
            self.image = self.current_frames[int(self.frame_index)]
            return

        # --- Otherwise handle movement ---
        self.is_moving = False
        if keys[pygame.K_a]:
            self.pos.x -= self.speed * dt
            self.direction = "left"
            self.is_moving = True
        elif keys[pygame.K_d]:
            self.pos.x += self.speed * dt
            self.direction = "right"
            self.is_moving = True
        elif keys[pygame.K_w]:
            self.pos.y -= self.speed * dt
            self.direction = "up"
            self.is_moving = True
        elif keys[pygame.K_s]:
            self.pos.y += self.speed * dt
            self.direction = "down"
            self.is_moving = True

        # Update the rect to the new position
        self.rect.center = self.pos

        # Clamp the rect to the map boundaries
        self.rect.clamp_ip(self.bounds)
        self.pos.x = self.rect.centerx
        self.pos.y = self.rect.centery

        # Decide which frames to use and what speed to play them at
        if self.is_moving:
            if self.current_frames != self.walk_right and self.current_frames != self.walk_left:
                self.frame_index = 0  # Reset animation when switching
                self.time_accumulator = 0

            if self.direction == "left":
                self.current_frames = self.walk_left
            else:
                self.current_frames = self.walk_right
            self.current_frame_speed = self.walk_frame_speed
        else:
            if self.current_frames != self.idle_right and self.current_frames != self.idle_left:
                self.frame_index = 0  # Reset animation when switching
                self.time_accumulator = 0

            if self.direction == "left":
                self.current_frames = self.idle_left
            else:
                self.current_frames = self.idle_right
            self.current_frame_speed = self.idle_frame_speed

        # Animate the frames
        self.time_accumulator += dt
        if self.time_accumulator >= self.current_frame_speed:
            self.time_accumulator = 0
            self.frame_index = (self.frame_index + 1) % len(self.current_frames)
            self.image = self.current_frames[self.frame_index]