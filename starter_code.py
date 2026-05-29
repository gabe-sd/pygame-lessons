import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Name")
font = pygame.font.SysFont("monospace", 36)
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # input detection
    keys = pygame.key.get_pressed()


    # game logic here
    # YOUR CODE HERE

    # draw stuff here
    screen.fill((0, 0, 0))
    # YOUR CODE HERE

    # no more code after this
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
