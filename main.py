import pygame

#Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Set the title and logo of the window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/spaceship.png')
pygame.display.set_icon(icon)

# Add Player
playerImg = pygame.image.load('images/player.png')
playerX = 370
playerY = 480
# playerX_change = 0
# playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Keep game in an infinite loop
running = True
while running:
    # Fill the screen with a color
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the player on the screen
    player(playerX, playerY)

    pygame.display.update()