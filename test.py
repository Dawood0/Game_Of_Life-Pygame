import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400




pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
SCREEN.fill(BLACK)


def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)            # 0 is for a solid full colored rectangle , 1 is for hollow rectangle (border only)

def drawRect(x,y,i=0,color=WHITE):
    blockSize = 20  # Set the size of the grid block
    rect = pygame.Rect(x, y, blockSize, blockSize)
    pygame.draw.rect(SCREEN, color, rect, i)            # 0 is for a solid full colored rectangle , 1 is for hollow rectangle (border only)

white_rects=[]
black_rects=[]                  # rectangles returning to black after being pressed while white



while True:
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        # mouse pos if clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            x,y=pygame.mouse.get_pos()
            x=(x//20)*20
            y=(y//20)*20
            print(x,y)
            if (x,y) not in white_rects:
                white_rects.append((x,y))
                try:black_rects.remove((x,y))
                except:pass
            else:
                black_rects.append((x, y))
                white_rects.remove((x,y))

        # if event.type == pygame.KEYDOWN:                # next step in the game (next state)
        #     if event.key == pygame.K_SPACE:
        #





    for x,y in white_rects:                 # drawing the white rectangle in the pressed rectangle
        drawRect(x,y)
    for x, y in black_rects:                # redrawing the black rectangle in the repressed rectangle
        drawRect(x, y,0,BLACK)
        drawRect(x, y,1)

    pygame.display.update()




