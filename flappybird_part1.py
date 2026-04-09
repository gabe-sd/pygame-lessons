# =============================================================================
# FLAPPY BIRD - Part 1
# =============================================================================
# SPACE = flap (push the bird up)
# Fly through the gaps between pipes without hitting anything.
# After game over, press SPACE to play again.
# =============================================================================

import pygame
import random

# Start pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Flappy Bird")

# Clock controls game speed
clock = pygame.time.Clock()

# Colors are (Red, Green, Blue) from 0-255
SKY_BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
YELLOW = (255, 230, 0)
WHITE = (255, 255, 255)

# Font for drawing the score and game over text
font = pygame.font.Font(None, 64)

# --- Bird setup ---
# pygame.Rect(x, y, width, height)
bird = pygame.Rect(100, 300, 30, 30)

# How fast the bird is moving up or down (negative = up, positive = down)
bird_speed = 0

# Gravity pulls the bird down a little more each frame
gravity = 0.4

# How strong a flap is (negative number = pushes bird upward)
flap_power = -8

# --- Pipe settings ---
PIPE_WIDTH = 60      # How wide each pipe is
PIPE_GAP = 160       # Space between the top and bottom pipe
PIPE_SPEED = 3       # How fast pipes move to the left

# Two lists to hold the pipes currently on the screen.
# top_pipes[0] always matches bottom_pipes[0] (they are a pair).
top_pipes = []
bottom_pipes = []

# Counts frames so we know when to spawn the next pipe pair
pipe_timer = 0

# Player's score
score = 0

# Is the game over right now?
game_over = False

# --- Game Loop ---
# This runs 60 times per second until the player quits.
# Every loop: check input, move things, draw everything.

running = True
while running:
    # -- Check for events --
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # SPACE flaps the bird, or restarts the game after game over
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_over:
                # Reset everything back to the start
                bird.center = (100, 300)
                bird_speed = 0
                top_pipes = []
                bottom_pipes = []
                pipe_timer = 0
                score = 0
                game_over = False
            else:
                # Flap! Push the bird upward.
                bird_speed = flap_power

    # Only update the game while it's still running
    if not game_over:
        # -- Move the bird --
        # Gravity makes the bird fall faster each frame
        bird_speed += gravity
        bird.y += bird_speed

        # -- Spawn a new pipe pair every so often --
        pipe_timer += 1
        if pipe_timer >= 90:   # every 90 frames (about 1.5 seconds)
            pipe_timer = 0

            # Pick a random height for the top pipe
            top_height = random.randint(50, 350)

            # Top pipe starts at the top of the screen
            new_top = pygame.Rect(400, 0, PIPE_WIDTH, top_height)

            # Bottom pipe starts below the gap and goes to the bottom
            new_bottom = pygame.Rect(400, top_height + PIPE_GAP, PIPE_WIDTH, 600)

            top_pipes.append(new_top)
            bottom_pipes.append(new_bottom)

        # -- Move all the pipes to the left --
        for pipe in top_pipes:
            pipe.x -= PIPE_SPEED
        for pipe in bottom_pipes:
            pipe.x -= PIPE_SPEED

        # -- Remove pipes that have gone off the left side --
        # When a pipe leaves the screen, the player scored a point.
        if len(top_pipes) > 0 and top_pipes[0].right < 0:
            top_pipes.pop(0)
            bottom_pipes.pop(0)
            score += 1

        # -- Check if the bird hit any pipe --
        for pipe in top_pipes:
            if bird.colliderect(pipe):
                game_over = True
        for pipe in bottom_pipes:
            if bird.colliderect(pipe):
                game_over = True

        # -- Check if the bird hit the top or bottom of the screen --
        if bird.top <= 0 or bird.bottom >= 600:
            game_over = True

    # -- Draw everything --
    screen.fill(SKY_BLUE)

    # Draw all the pipes
    for pipe in top_pipes:
        pygame.draw.rect(screen, GREEN, pipe)
    for pipe in bottom_pipes:
        pygame.draw.rect(screen, GREEN, pipe)

    # Draw the bird
    pygame.draw.rect(screen, YELLOW, bird)

    # Draw the score at the top of the screen
    score_text = font.render(str(score), True, WHITE)
    screen.blit(score_text, (185, 20))

    # Draw the game over message in the middle
    if game_over:
        over_text = font.render("Game Over", True, WHITE)
        screen.blit(over_text, (70, 270))

    # Show what we drew
    pygame.display.flip()

    # Run at 60 frames per second
    clock.tick(60)

pygame.quit()
