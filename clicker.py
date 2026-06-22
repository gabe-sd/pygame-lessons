# =====================================================
# Clicker Game  |  Part 1
# =====================================================

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker")
font = pygame.font.SysFont("monospace", 36)
clock = pygame.time.Clock()
FPS = 60

# --- button image ---
button_image = pygame.image.load("button.png")   # replace with your image filename
button_image = pygame.transform.scale(button_image, (200, 100))  # (width, height) in pixels

# get_rect() returns a Rect that is the same size as the image — pygame.Rect(x, y, w, h)
button_rect = button_image.get_rect()
button_rect.topleft = (50, 50)

# --- game state ---
count = 0

running = True
while running:
    # --- events ---
    # pygame.event.get() gives us a list of things that just happened this frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # MOUSEBUTTONDOWN fires ONCE when the player presses a mouse button
        # (unlike key.get_pressed() which is True every frame the key is held)
        if event.type == pygame.MOUSEBUTTONDOWN:
            # event.pos is a tuple (x, y) of where the click happened on screen
            # collidepoint() checks if that point is inside the button's rect
            if button_rect.collidepoint(event.pos):
                count = count + 1

    # --- held keys ---
    keys = pygame.key.get_pressed()

    # --- game logic ---

    # --- draw ---
    screen.fill((0, 0, 0))

    # screen.blit() copies the image onto the screen at the position of button_rect
    screen.blit(button_image, button_rect)

    text = font.render("Clicks: " + str(count), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # no more code after this
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
