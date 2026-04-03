# =============================================================================
# PONG - Part 2
# =============================================================================
# Player 1 (Left):  W = up, S = down
# Player 2 (Right): UP arrow = up, DOWN arrow = down
# =============================================================================

# ======================== NEW IN PART 2 ========================
#   1. Win condition  -- first to 3 points wins
#   2. Post-point pause -- ball holds for 1 second after each score
#   3. Game over screen -- shows winner and a SPACE-to-restart prompt
# ===============================================================

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

# Fonts
large_font = pygame.font.Font(None, 64)  # renamed from 'font' in Part 1
small_font = pygame.font.Font(None, 36)  # <-- NEW: smaller font for the restart message

# --- NEW IN PART 2: game state ---
WINNING_SCORE = 3   # <-- NEW: game ends when someone reaches this score
game_over = False   # <-- NEW: stops input and movement when True
pause_until = 0     # <-- NEW: timestamp; ball waits until this passes

# --- Create game objects using Rectangles ---
# pygame.Rect(x, y, width, height)
# x goes left to right, y goes top to bottom

# Left paddle
paddle1 = pygame.Rect(30, 250, 15, 90)

# Right paddle
paddle2 = pygame.Rect(755, 250, 15, 90)

# Ball (starts in the center)
ball = pygame.Rect(392, 292, 15, 15)

# Ball speed (how many pixels it moves each frame)
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

        # ===== NEW IN PART 2: press SPACE to restart after game over =====
        # KEYDOWN fires once when a key is first pressed (unlike get_pressed)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                # Reset everything for a new game
                score1 = 0
                score2 = 0
                game_over = False
                ball.center = (400, 300)
                ball_speed_x = 4
                ball_speed_y = 4
                paddle1.centery = 300
                paddle2.centery = 300
                pause_until = 0

    # -- Check which keys are held down --
    keys = pygame.key.get_pressed()

    # ===== NEW IN PART 2: freeze paddle input once game is over =====
    if not game_over:

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

    # ===== NEW IN PART 2: hold ball during post-point pause and after game over =====
    if not game_over and pygame.time.get_ticks() >= pause_until:

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
            # ===== NEW IN PART 2: check win, otherwise start 1-second pause =====
            if score2 >= WINNING_SCORE:
                game_over = True
            else:
                pause_until = pygame.time.get_ticks() + 1000  # 1000 ms = 1 second

        # Ball goes off right side - Player 1 scores
        if ball.left >= 800:
            score1 += 1
            ball.center = (400, 300)
            ball_speed_x = -ball_speed_x
            # ===== NEW IN PART 2: check win, otherwise start 1-second pause =====
            if score1 >= WINNING_SCORE:
                game_over = True
            else:
                pause_until = pygame.time.get_ticks() + 1000  # 1000 ms = 1 second

    # -- Draw everything --
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.rect(screen, WHITE, ball)

    # Draw scores
    text1 = large_font.render(str(score1), True, WHITE)
    text2 = large_font.render(str(score2), True, WHITE)
    screen.blit(text1, (200, 20))
    screen.blit(text2, (580, 20))

    # ===== NEW IN PART 2: overlay winner text and restart prompt =====
    if game_over:
        if score1 >= WINNING_SCORE:
            win_text = large_font.render("P1 Wins!", True, WHITE)
        else:
            win_text = large_font.render("P2 Wins!", True, WHITE)
        screen.blit(win_text, (400 - win_text.get_width() // 2, 250))

        restart_text = small_font.render("Press SPACE to restart", True, WHITE)
        screen.blit(restart_text, (400 - restart_text.get_width() // 2, 320))

    # Show what we drew
    pygame.display.flip()

    # Run at 60 frames per second
    clock.tick(60)

pygame.quit()
