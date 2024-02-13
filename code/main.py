import random

import pygame
import sys

from pokethon import Pokethon

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Character Movement")
venusaur = Pokethon("Venusaur", "003", None)
ivysaur = Pokethon("Ivysaur", "002", venusaur)
bulbasaur = Pokethon("Bulbasaur", "001", ivysaur)
charizard = Pokethon("Charizard", "006", None)
charmeleon = Pokethon("Charmeleon", "005", charizard)
charmander = Pokethon("Charmander", "004", charmeleon)
blastoise = Pokethon("Blastoise", "009", None)
wartortle = Pokethon("Wartortle", "008", blastoise)
squirtle = Pokethon("Squirtle", "007", wartortle)
paused = False
fight = False
inventory = False

available_pokethons = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise]

# Load player images
player_images = {
    "down_idle": pygame.image.load("../res/art/pokethon_player/Pokethon_player1.png"),
    "down_1": pygame.image.load("../res/art/pokethon_player/Pokethon_player2.png"),
    "down_2": pygame.image.load("../res/art/pokethon_player/Pokethon_player3.png"),
    "up_idle": pygame.image.load("../res/art/pokethon_player/Pokethon_player4.png"),
    "up_1": pygame.image.load("../res/art/pokethon_player/Pokethon_player5.png"),
    "up_2": pygame.image.load("../res/art/pokethon_player/Pokethon_player6.png"),
    "left_idle": pygame.image.load("../res/art/pokethon_player/Pokethon_player7.png"),
    "left_1": pygame.image.load("../res/art/pokethon_player/Pokethon_player8.png"),
    "left_2": pygame.image.load("../res/art/pokethon_player/Pokethon_player9.png"),
    "right_idle": pygame.image.load("../res/art/pokethon_player/Pokethon_player10.png"),
    "right_1": pygame.image.load("../res/art/pokethon_player/Pokethon_player11.png"),
    "right_2": pygame.image.load("../res/art/pokethon_player/Pokethon_player12.png"),

}

background_inner = pygame.image.load("../res/art/bg/map_inner.png")
background_inner = pygame.transform.scale(background_inner, (WIDTH, HEIGHT))

background_outer = pygame.image.load("../res/art/bg/map_outer.png")
background_outer = pygame.transform.scale(background_outer, (WIDTH, HEIGHT))

pyplay_group = pygame.sprite.Group()

curr_pokethon = None


class PyPlay(pygame.sprite.Sprite):
    def __init__(self, pokethon):
        super().__init__()
        self.pokethon = pokethon
        self.image = pokethon.get_image()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

    def update(self):
        self.rect.y += 1
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0


def spawn_pyplay():
    random_pokethon = random.choice(available_pokethons)
    pyplay = PyPlay(random_pokethon)
    pyplay_group.add(pyplay)


def show_inventory():
    global paused
    global inventory
    pass


def catch_pokethona(pokethon):
    global paused
    global fight
    for i in range(1, 6):
        catch_bg = pygame.image.load("../res/art/bg/catch_bg.png")
        catch_bg = pygame.transform.scale(catch_bg, (WIDTH, HEIGHT))
        screen.blit(catch_bg, (0, 0))  # Adjust coordinates as needed
        curr_anim = pygame.image.load("../res/art/player_throw/throw" + str(i) + ".png")
        curr_anim = pygame.transform.scale(curr_anim, (WIDTH / 3, WIDTH / 3))
        screen.blit(curr_anim, (0, HEIGHT - curr_anim.get_height()))
        poke = pygame.transform.scale(pokethon.image, (pokethon.image.get_width() * 2, pokethon.image.get_height() * 2))
        screen.blit(poke, (WIDTH - 300, 100))
        if i > 3:
            pokeball = pygame.image.load("../res/art/assets/pokeball.png")
            pokeball = pygame.transform.scale(pokeball, (40, 40))
            screen.blit(pokeball, (0 + (i - 2) * 180, HEIGHT - curr_anim.get_height() - 70 * (i - 3)))
        pygame.display.flip()
        pygame.time.delay(500)
    catch_bg = pygame.image.load("../res/art/bg/catch_bg.png")
    catch_bg = pygame.transform.scale(catch_bg, (WIDTH, HEIGHT))
    screen.blit(catch_bg, (0, 0))  # Adjust coordinates as needed
    curr_anim = pygame.image.load("../res/art/player_throw/throw5.png")
    curr_anim = pygame.transform.scale(curr_anim, (WIDTH / 3, WIDTH / 3))
    screen.blit(curr_anim, (0, HEIGHT - curr_anim.get_height()))
    bang = pygame.image.load("../res/art/assets/BANG.png")
    bang = pygame.transform.scale(bang, (pokethon.image.get_width() * 2, pokethon.image.get_height() * 2))
    screen.blit(bang, (WIDTH - 300, 100))
    pygame.display.flip()
    pygame.time.delay(500)
    paused = False
    fight = False


SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 5000)

# Set up the player position and speed
player_width, player_height = 40, 60
player_x, player_y = (WIDTH - player_width) // 2, (HEIGHT - player_height) // 2
player_speed = 5

# Initialize variables for animation
frame_count = 0
animation_speed = 10  # Adjust animation speed by changing the value
direction = 270

# Create a sprite group for the player
player_group = pygame.sprite.GroupSingle()

current_image = player_images["down_idle"]

# Create the player sprite
player_sprite = pygame.sprite.Sprite()
player_sprite.image = current_image  # Use the current image of the player
player_sprite.rect = current_image.get_rect()
player_sprite.rect.center = (WIDTH // 2, HEIGHT // 2)  # Center the player on the screen
player_group.add(player_sprite)

# Cap the frame rate
pygame.time.Clock().tick(60)

# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_EVENT:
            spawn_pyplay()

    keys = pygame.key.get_pressed()
    if not paused:
        if keys[pygame.K_LEFT]:
            player_sprite.rect.x -= player_speed
            moving = True
            direction = 180
        if keys[pygame.K_RIGHT]:
            player_sprite.rect.x += player_speed
            moving = True
            direction = 0
        if keys[pygame.K_UP]:
            player_sprite.rect.y -= player_speed
            moving = True
            direction = 90
        if keys[pygame.K_DOWN]:
            player_sprite.rect.y += player_speed
            moving = True
            direction = 270

    if not any(keys):
        moving = False

    # Boundaries to keep the player within the screen
    player_sprite.rect.x = max(0, min(player_sprite.rect.x, WIDTH - player_width))
    player_sprite.rect.y = max(0, min(player_sprite.rect.y, HEIGHT - player_height))

    if moving:
        frame_count += 1
        if direction == 270:
            if frame_count // animation_speed % 2 == 0:
                current_image = player_images["down_1"]
            else:
                current_image = player_images["down_2"]
        elif direction == 90:
            if frame_count // animation_speed % 2 == 0:
                current_image = player_images["up_1"]
            else:
                current_image = player_images["up_2"]
        elif direction == 0:
            if frame_count // animation_speed % 2 == 0:
                current_image = player_images["right_1"]
            else:
                current_image = player_images["right_2"]
        elif direction == 180:
            if frame_count // animation_speed % 2 == 0:
                current_image = player_images["left_1"]
            else:
                current_image = player_images["left_2"]
    else:
        if direction == 270:
            current_image = player_images["down_idle"]
        elif direction == 90:
            current_image = player_images["up_idle"]
        elif direction == 0:
            current_image = player_images["right_idle"]
        elif direction == 180:
            current_image = player_images["left_idle"]

    current_image = pygame.transform.scale(current_image, (player_width, player_height))

    # Calculate the camera offset
    camera_offset_x = player_sprite.rect.x - (WIDTH // 2)
    camera_offset_y = player_sprite.rect.y - (HEIGHT // 2)

    screen.blit(background_outer, (0, 0))
    # Draw the background with camera offset
    screen.blit(background_inner, (-camera_offset_x, -camera_offset_y))

    # Draw the player at the center of the screen
    screen.blit(current_image, (WIDTH // 2 - player_width // 2, HEIGHT // 2 - player_height // 2))

    if not paused:
        for pyplay in pyplay_group:
            screen.blit(pyplay.image, (pyplay.rect.x - camera_offset_x, pyplay.rect.y - camera_offset_y))

    # Check for collisions between player and PyPlay objects
    collisions = pygame.sprite.spritecollide(player_sprite, pyplay_group, True)

    # Perform actions when a collision is detected
    for collision in collisions:
        print("Collision with", collision.pokethon.name)  # Example action, replace with your own logic
        curr_pokethon = collision.pokethon
        paused = True
        fight = True

    if paused:
        if fight:
            catch_pokethona(curr_pokethon)
        if inventory:
            show_inventory()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
