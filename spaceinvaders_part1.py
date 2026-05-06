# =============================================================================
# SPACE INVADERS - Part 1
# =============================================================================
# LEFT / RIGHT arrows = move the ship
# SPACE = shoot (one bullet on screen at a time)
# Hit the enemies with your bullets. Once an enemy is shot it does not come back.
# =============================================================================

import pygame

# Start pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Space Invaders")

# Clock controls game speed
clock = pygame.time.Clock()

# Colors are (Red, Green, Blue) from 0-255
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Font for drawing the score
font = pygame.font.Font(None, 36)

# --- Player ship ---
# pygame.Rect(x, y, width, height)
player = pygame.Rect(280, 540, 40, 20)

# --- Bullet ---
# Only one bullet is allowed on screen at a time.
# When bullet is None it means there is no bullet right now.
bullet = None

# --- Enemies ---
# Build a list of 8 enemies in a row near the top of the screen.
# Each enemy is its own pygame.Rect so we can move it and check collisions.
enemies = []
for i in range(8):
    x = 50 + i * 60     # space them out across the screen
    y = 100
    enemies.append(pygame.Rect(x, y, 40, 25))

# All enemies move together as a group.
# 1 means moving right, -1 means moving left.
enemy_direction = 1

# Player's score
score = 0

# --- Game Loop ---
# This runs 60 times per second until the player quits.
# Every loop: check input, move things, draw everything.

running = True
while running:
    # -- Check for events --
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # SPACE fires a bullet, but only if there isn't one already on screen.
        # KEYDOWN fires once when the key is first pressed (not while held).
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if bullet is None:
                # Start the bullet just above the player ship.
                # centerx is the middle of the player; the - 3 shifts left
                # so the 6-wide bullet ends up centered on the ship.
                bullet = pygame.Rect(player.centerx - 3, player.top - 12, 6, 12)

    # -- Check which keys are held down --
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < 600:
        player.x += 5

    # -- Move the bullet --
    if bullet is not None:
        bullet.y -= 8                # in pygame, smaller y = higher on screen
        if bullet.bottom < 0:        # bullet flew off the top of the screen
            bullet = None

    # -- Move all enemies sideways --
    for enemy in enemies:
        enemy.x += 2 * enemy_direction

    # If any enemy touches a wall, flip the direction for the whole group
    for enemy in enemies:
        if enemy.right >= 600 or enemy.left <= 0:
            enemy_direction = -enemy_direction
            break    # only flip once, even if several enemies hit the edge

    # -- Check if the bullet hit an enemy --
    if bullet is not None:
        for enemy in enemies:
            if bullet.colliderect(enemy):     # True when two Rects overlap
                enemies.remove(enemy)         # destroy the enemy
                bullet = None                 # destroy the bullet
                score += 1
                break    # MUST break: we just changed the list we are looping over

    # -- Draw everything --
    screen.fill(BLACK)

    # Player ship
    pygame.draw.rect(screen, GREEN, player)

    # Bullet (only if it exists)
    if bullet is not None:
        pygame.draw.rect(screen, YELLOW, bullet)

    # Each enemy
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Score in the top-left corner
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Show what we drew
    pygame.display.flip()

    # Run at 60 frames per second
    clock.tick(60)

pygame.quit()
