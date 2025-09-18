import pygame
from player import Player
from wolf import Wolf
from bird import Bird
from static_entity import StaticEntity
from tile_map import TileMap
from camera import Camera

pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wolf Game")
clock = pygame.time.Clock()
running = True
dt = 0

wolf1 = Wolf(pos=(640, 360), speed=100, x_range=(200, 800))
wolf2 = Wolf(pos=(500, 400), speed=150, x_range=(100, 600))
bluejay = Bird(pos=(350, 100), speed=150, x_range=(300, 550))
whitebird = Bird(pos=(800, 150), speed=150, x_range=(700, 900), bird_type=1)
redbird = Bird(pos=(600, 175), speed=150, x_range=(500, 900), bird_type=2)
campfire = StaticEntity(pos=(500, 500), entity_type=0)
marketplace = StaticEntity(pos=(200, 400), entity_type=1)
crops = StaticEntity(pos=(400, 380), entity_type=2)
tree = StaticEntity(pos=(400, 230), entity_type=3)

tilemap = TileMap(filename="MapGrid.txt")
map_width, map_height = tilemap.get_map_size()

player = Player(pos=(600, 600), bounds=(0, 0, map_width, map_height))
all_sprites = pygame.sprite.Group(wolf1, wolf2, player, bluejay, whitebird, redbird, campfire, marketplace, crops, tree)

# Pass map dimensions to the camera
camera = Camera(screen_width, screen_height, map_width, map_height)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.handle_event(event)

    keys = pygame.key.get_pressed()

    player.update(dt, keys)
    wolf1.update(dt, keys)
    wolf2.update(dt, keys)
    bluejay.update(dt, keys)
    whitebird.update(dt, keys)
    redbird.update(dt, keys)
    campfire.update(dt, keys)
    marketplace.update(dt, keys)
    crops.update(dt, keys)
    tree.update(dt, keys)

    camera.update(player)

    screen.fill('Blue')

    tilemap.draw(screen, camera)

    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite.rect))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()