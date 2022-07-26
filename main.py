import random
import math

import pygame
from pygame import mixer

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background image
background = pygame.image.load('images/background.png')

# Backgroun music
mixer.music.load('sounds/background.wav')
mixer.music.play(-1)

# Set the title and logo of the window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/spaceship.png')
pygame.display.set_icon(icon)

# Add Player
playerImg = pygame.image.load('images/player2.png')
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 370
playerY = 480
playerX_change = 0

# Add Mutiple Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
for i in range(6):
    enemyImg.append(pygame.image.load('images/enemy.png'))
    enemyImg[i] = pygame.transform.scale(enemyImg[i], (58, 58))
    enemyX.append(random.randint(0, 740))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1.5)
    enemyY_change.append(30)


# Add Bullet
bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Add score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Function to show score on the screen
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))

# Function to draw the player on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))


# Function to draw the enemy on the screen
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# Function to fire bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Function to implement collision
def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Keep game in an infinite loop until closed
running = True
while running:
    # Fill the screen with a background color
    screen.fill((0, 0, 0))

    # Draw the background image
    screen.blit(background, (0, 0))

    # Add event to close game when user clicks the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Add keystroke event for when the left or right keys are pressed
        if event.type == pygame.KEYDOWN:
            # Player should move left when the left arrow is pressed
            if event.key == pygame.K_LEFT:
                playerX_change = -2.8

            # Player should move right when the right arrow is pressed
            if event.key == pygame.K_RIGHT:
                playerX_change = 2.8

            # Bullet should fire when player presses the space bar
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = pygame.mixer.Sound('sounds/laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

    # Add keystroke event for when the left or right keys are released
    if event.type == pygame.KEYUP:
        # Player should stop moving when left or right arrow is released
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    # Move the player on the screen
    playerX += playerX_change

    # Check if the player is out of the screen
    if playerX <= 0:
        playerX = 0
    elif playerX >= 742:
        playerX = 742

    # Move the enemy on the screen
    for i in range(6):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 740:
            enemyX_change[i] = -1.5
            enemyY[i] += enemyY_change[i]

        # Check if the enemy is out of the screen
        if enemyY[i] >= 450:
            for j in range(6):
                enemyY[j] = 2000
            game_over_text()
            break

        # Check if the enemy and player collide
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 740)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)


    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Draw the player on the screen
    player(playerX, playerY)

    # Draw the score on the screen
    show_score(textX, textY)

    # Update the screen
    pygame.display.update()
