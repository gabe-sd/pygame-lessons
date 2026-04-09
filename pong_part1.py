# =============================================================================
# PONG - Part 1
# =============================================================================
# Player 1 (Left):  W = up, S = down
# Player 2 (Right): UP arrow = up, DOWN arrow = down
# =============================================================================

import pygame

# Start pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

# Clock controls game speed
clock = pygame.time.Clock()

# Colors are (Red, Green, Blue) from 0-255
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font for drawing the score
font = pygame.font.Font(None, 64)

# --- Create game objects using Rectangles ---
# pygame.Rect(x, y, width, height)

# Left paddle
paddle1 = pygame.Rect(30, 250, 15, 90)

# Right paddle
paddle2 = pygame.Rect(755, 250, 15, 90)

# Ball (starts in the center)
ball = pygame.Rect(392, 292, 15, 15)

# Ball speed (pixels per frame)
ball_speed_x = 4
ball_speed_y = 4

# Scores
score1 = 0
score2 = 0

# --- Game Loop ---
# This runs 60 times per second until the player quits.
# Every loop: check input, move things, draw everything.

running = True
while running:
    # -- Check for events --
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -- Check which keys are held down --
    keys = pygame.key.get_pressed()

    # Player 1: W and S
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= 5
    if keys[pygame.K_s] and paddle1.bottom < 600:
        paddle1.y += 5

    # Player 2: Arrow keys
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= 5
    if keys[pygame.K_DOWN] and paddle2.bottom < 600:
        paddle2.y += 5

    # -- Move the ball --
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce off top and bottom walls
    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed_y = -ball_speed_y

    # Bounce off paddles
    if ball.colliderect(paddle1) and ball_speed_x < 0:
        ball_speed_x = -ball_speed_x
    if ball.colliderect(paddle2) and ball_speed_x > 0:
        ball_speed_x = -ball_speed_x

    # Ball goes off left side - Player 2 scores
    if ball.right <= 0:
        score2 += 1
        ball.center = (400, 300)
        ball_speed_x = -ball_speed_x

    # Ball goes off right side - Player 1 scores
    if ball.left >= 800:
        score1 += 1
        ball.center = (400, 300)
        ball_speed_x = -ball_speed_x

    # -- Draw everything --
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.rect(screen, WHITE, ball)

    # Draw scores
    text1 = font.render(str(score1), True, WHITE) #(255, 255, 255)
    text2 = font.render(str(score2), True, WHITE)
    screen.blit(text1, (200, 20))
    screen.blit(text2, (580, 20))

    # Show what we drew
    pygame.display.flip()

    # Run at 60 frames per second
    clock.tick(60)

pygame.quit()
