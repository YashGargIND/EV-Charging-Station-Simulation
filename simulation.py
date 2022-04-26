import pygame
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512 + 50

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("simulation")
clock = pygame.time.Clock()

# ---------------------------------------------------------------------------------------------------------
        # Game specific variables
exitGame = False

walls = [
        [(1,1,1,0),(1,0,0,1),(1,1,0,0),(1,0,1,0),(1,0,1,0),(1,0,1,0),(1,1,0,0),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        [(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()],
        ]

path = 'ssssdadswsdwaasd'
i = 0

BLOCK_SIZE = 512/16
x = 0*BLOCK_SIZE
y = 0*BLOCK_SIZE

batteryPercentage = 100

gameFont = pygame.font.Font('Merriweather-Bold.ttf',20)

charging_stations = [(12*BLOCK_SIZE,15*BLOCK_SIZE), (6*BLOCK_SIZE,9*BLOCK_SIZE), (10*BLOCK_SIZE,4*BLOCK_SIZE), (7*BLOCK_SIZE,13*BLOCK_SIZE)]
# ----------------------------------------------------------------------------------------------------------
            # GAME ASSETS
            # background
maze = pygame.image.load('img/maze.png').convert()
maze = pygame.transform.scale(maze, (512,512))

power = pygame.image.load('img/Power.png').convert_alpha()
power = pygame.transform.scale(power, (int(452/32), int(980/32)))


# -------------------------------------------------------------------------------------------------------
            # GAME LOOP
while not exitGame:
            # Event Checker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        pygame.draw.rect(maze, (255, 255, 255), [x + BLOCK_SIZE/4 -0.5,y + BLOCK_SIZE/4 - 1, BLOCK_SIZE/1.5, BLOCK_SIZE/1.5])
                        pygame.draw.rect(maze, 'black', [x + BLOCK_SIZE/2,y + BLOCK_SIZE/2, BLOCK_SIZE/5, BLOCK_SIZE/5])
                        letter = path[i]
                        if letter == 'd':
                                x = x + BLOCK_SIZE
                        if letter == 'w':
                               y = y - BLOCK_SIZE
                        if letter == 'a':
                               x = x - BLOCK_SIZE
                        if letter == 's':
                               y = y + BLOCK_SIZE
                        i = i+1
                        batteryPercentage -=2   
                if event.key == pygame.K_d:
                        pygame.draw.rect(maze, (255, 255, 255), [x + BLOCK_SIZE/4 -0.5,y + BLOCK_SIZE/4 - 1, BLOCK_SIZE/1.5, BLOCK_SIZE/1.5])
                        pygame.draw.rect(maze, 'black', [x + BLOCK_SIZE/2,y + BLOCK_SIZE/2, BLOCK_SIZE/5, BLOCK_SIZE/5])
                        x = x + BLOCK_SIZE
                        batteryPercentage -=2
                if event.key == pygame.K_w:
                        pygame.draw.rect(maze, (255, 255, 255), [x + BLOCK_SIZE/4 -0.5,y + BLOCK_SIZE/4 - 1, BLOCK_SIZE/1.5, BLOCK_SIZE/1.5])
                        pygame.draw.rect(maze, 'black', [x + BLOCK_SIZE/2,y + BLOCK_SIZE/2, BLOCK_SIZE/5, BLOCK_SIZE/5])
                        y = y - BLOCK_SIZE
                        batteryPercentage -=2
                if event.key == pygame.K_a:
                        pygame.draw.rect(maze, (255, 255, 255), [x + BLOCK_SIZE/4 -0.5,y + BLOCK_SIZE/4 - 1, BLOCK_SIZE/1.5, BLOCK_SIZE/1.5])
                        pygame.draw.rect(maze, 'black', [x + BLOCK_SIZE/2,y + BLOCK_SIZE/2, BLOCK_SIZE/5, BLOCK_SIZE/5])
                        x = x - BLOCK_SIZE
                        batteryPercentage -=2
                if event.key == pygame.K_s:
                        pygame.draw.rect(maze, (255, 255, 255), [x + BLOCK_SIZE/4 -0.5,y + BLOCK_SIZE/4 - 1, BLOCK_SIZE/1.5, BLOCK_SIZE/1.5])
                        pygame.draw.rect(maze, 'black', [x + BLOCK_SIZE/2,y + BLOCK_SIZE/2, BLOCK_SIZE/5, BLOCK_SIZE/5])
                        y = y + BLOCK_SIZE
                        batteryPercentage -=2
        if (x,y) in charging_stations:
                batteryPercentage = 100
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            # BackGround
    screen.fill((255, 236, 179))
    screen.blit(maze, (0, 0))
    pygame.draw.rect(maze, (255, 0, 0), [x + BLOCK_SIZE/4 -0.5,y + BLOCK_SIZE/4 - 1, BLOCK_SIZE/1.5, BLOCK_SIZE/1.5])
    for position in charging_stations:
            screen.blit(power, (position[0]+ BLOCK_SIZE/4 , position[1]))
    
    Name_surface1 = gameFont.render('Battery Left : ' + str(batteryPercentage) + '%', True,'black')
    name_rect1 = Name_surface1.get_rect(center=(400, 535))    
    screen.blit(Name_surface1, name_rect1)
#     print(str(x) + str(y))
    pygame.display.update()
    clock.tick(120)
# -----------------------------------------------------------------------------------------------------------
pygame.quit()
quit()

# -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x--x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
