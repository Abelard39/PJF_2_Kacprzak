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

background_image = pygame.image.load("../res/art/background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


# Set up the player position and speed
player_width, player_height = 40, 60
player_x, player_y = (WIDTH - player_width) // 2, (HEIGHT - player_height) // 2
player_speed = 5

# Initialize variables for animation
frame_count = 0
animation_speed = 10  # Adjust animation speed by changing the value
direction = 270

# Main game loop
running = True
moving = False  # Flag to check if the player is moving
while running:
    screen.fill((255, 255, 255))

    # Draw the background
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of the arrow keys
    keys = pygame.key.get_pressed()

    # Update player position based on arrow key presses
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        moving = True
        direction = 180
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        moving = True
        direction = 0
    if keys[pygame.K_UP]:
        player_y -= player_speed
        moving = True
        direction = 90
    if keys[pygame.K_DOWN]:
        player_y += player_speed
        moving = True
        direction = 270

    if not any(keys):
        moving = False

    # Boundaries to keep the player within the screen
    player_x = max(0, min(player_x, WIDTH - player_width))
    player_y = max(0, min(player_y, HEIGHT - player_height))

    # Display appropriate player image based on movement
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

    # Draw the player
    screen.blit(current_image, (player_x, player_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
