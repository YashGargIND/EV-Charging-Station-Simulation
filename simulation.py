import pygame

pygame.init()
screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption("simulation")
clock = pygame.time.Clock()

# ---------------------------------------------------------------------------------------------------------
        # Game specific variables
exitGame = False
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

BLOCK_SIZE = 512/16
x = 0*BLOCK_SIZE
y = 0*BLOCK_SIZE

charging_stations = [(12*BLOCK_SIZE,15*BLOCK_SIZE), (6*BLOCK_SIZE,9*BLOCK_SIZE), (10*BLOCK_SIZE,4*BLOCK_SIZE), (7*BLOCK_SIZE,13*BLOCK_SIZE)]
# ----------------------------------------------------------------------------------------------------------
            # GAME ASSETS
            # background
maze = pygame.image.load('img/maze.png').convert()
maze = pygame.transform.scale(maze, (512,512))

power = pygame.image.load('img/Power.png').convert_alpha()
power = pygame.transform.scale(power, (452/32, 980/32))
# powerRect = []
# for position in charging_stations:
#         powerRect.append(maze.get_rect(center = (position[0]+BLOCK_SIZE/2, position[1])))
# class car(object):
#         def _init_(self):
#                 self.color = (255,0,0)
#                 self.position = (0,0)
#         def draw(self, surface):
#                 r = pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE))
#                 pygame.draw.rect(surface, self.color, r)

# CAR = car()
# -------------------------------------------------------------------------------------------------------
            # GAME LOOP
while not exitGame:
            # Event Checker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                    pygame.draw.rect(maze, (255, 255, 255), [x + BLOCK_SIZE/4 -0.5,y + BLOCK_SIZE/4 - 1, BLOCK_SIZE/1.5, BLOCK_SIZE/1.5])
                    x = x + BLOCK_SIZE
            if event.key == pygame.K_w:
                    pygame.draw.rect(maze, (255, 255, 255), [x + BLOCK_SIZE/4 -0.5,y + BLOCK_SIZE/4 - 1, BLOCK_SIZE/1.5, BLOCK_SIZE/1.5])
                    y = y - BLOCK_SIZE
            if event.key == pygame.K_a:
                    pygame.draw.rect(maze, (255, 255, 255), [x + BLOCK_SIZE/4 -0.5,y + BLOCK_SIZE/4 - 1, BLOCK_SIZE/1.5, BLOCK_SIZE/1.5])
                    x = x - BLOCK_SIZE
            if event.key == pygame.K_s:
                    pygame.draw.rect(maze, (255, 255, 255), [x + BLOCK_SIZE/4 -0.5,y + BLOCK_SIZE/4 - 1, BLOCK_SIZE/1.5, BLOCK_SIZE/1.5])
                    y = y + BLOCK_SIZE
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # BackGround
    screen.blit(maze, (0, 0))
    pygame.draw.rect(maze, (255, 0, 0), [x + BLOCK_SIZE/4 -0.5,y + BLOCK_SIZE/4 - 1, BLOCK_SIZE/1.5, BLOCK_SIZE/1.5])
    for position in charging_stations:
            screen.blit(power, (position[0]+ BLOCK_SIZE/4 , position[1]))
    pygame.display.update()
    clock.tick(120)
# -----------------------------------------------------------------------------------------------------------
pygame.quit()
quit()

# -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
