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
playerX_change = 0
# playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Keep game in an infinite loop
running = True
while running:
    # Fill the screen with a color
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        """" Close game event for when 
        the user clicks the close button """
        if event.type == pygame.QUIT:
            running = False

    """ add keystroke event for when the left or right keys are pressed """
    if event.type == pygame.KEYDOWN:
        """ When the left arrow is pressed """
        if event.key == pygame.K_LEFT:
            playerX_change = -0.3

        """ When the right arrow is pressed """
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.3

    """ add keystroke event for when the left or right keys are released """
    if event.type == pygame.KEYUP:
        """ Player shouldnt move on the x axis when 
        left or right arrow is released """
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change
    # playerY += playerY_change

    # Draw the player on the screen
    player(playerX, playerY)

    pygame.display.update()