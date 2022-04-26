import pygame

pygame.init()
screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption("simulation")
clock = pygame.time.Clock()

# ---------------------------------------------------------------------------------------------------------
        # Game specific variables
exitGame = False

# ----------------------------------------------------------------------------------------------------------
            # GAME ASSETS
            # background
maze = pygame.image.load('img/maze.png').convert()
maze = pygame.transform.scale(maze, (512,512))

# -------------------------------------------------------------------------------------------------------
            # GAME LOOP
while not exitGame:
            # Event Checker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # BackGround
    screen.blit(maze, (0, 0))

    pygame.display.update()
    clock.tick(120)
# -----------------------------------------------------------------------------------------------------------
pygame.quit()
quit()

# -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
