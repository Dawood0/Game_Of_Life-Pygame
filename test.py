import time

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
blockSize = 20

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

def getNeighbors(rect):     # rect is a tuple of x,y coordinates for the rectangle
    neighbors=[]
    x,y=rect
    if y-blockSize>=0:neighbors.append((x,y-blockSize))
    if y+blockSize<WINDOW_HEIGHT:neighbors.append((x,y+blockSize))
    if x-blockSize>=0:neighbors.append((x-blockSize,y))
    if x+blockSize<WINDOW_WIDTH:neighbors.append((x+blockSize,y))

    if x-blockSize>=0 and y-blockSize>=0: neighbors.append((x-blockSize,y-blockSize))
    if x+blockSize<WINDOW_WIDTH and y-blockSize>=0: neighbors.append((x+blockSize,y-blockSize))
    if x - blockSize >= 0 and y + blockSize < WINDOW_HEIGHT: neighbors.append((x - blockSize, y + blockSize))
    if x + blockSize < WINDOW_WIDTH and y + blockSize < WINDOW_HEIGHT: neighbors.append((x + blockSize, y + blockSize))

    return neighbors


white_rects=[]
black_rects=[]                  # rectangles returning to black after being pressed while white

birth=[]
die=[]

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

            print("----")
            print(white_rects)
            print(black_rects)

            # print(pygame.mouse.get_pos())
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


            for x, y in black_rects:  # redrawing the black rectangle in the repressed rectangle
                drawRect(x, y, 0, BLACK)
                drawRect(x, y, 1)







        if event.type == pygame.KEYUP:                # next step in the game (next state)
            if event.key == pygame.K_SPACE:
                for ii in white_rects:
                    die=[]
                    cnt=0
                    l=getNeighbors(ii)

                    for i in l:
                        if i in white_rects:
                            print(i)
                            cnt+=1

                    if cnt<2:
                        black_rects.append(ii)
                        # if ii not in black_rects:black_rects.append(ii)
                        # else:black_rects.remove(ii)
                        # try:white_rects.remove(ii)
                        # except:pass









    for x,y in white_rects:                 # drawing the white rectangle in the pressed rectangle
        drawRect(x,y)
    # for x, y in black_rects:                # redrawing the black rectangle in the repressed rectangle
    #     drawRect(x, y,0,BLACK)
    #     drawRect(x, y,1)
    #
    for i in range(len(black_rects)):
        x,y=black_rects.pop()
        drawRect(x, y,0,BLACK)
        drawRect(x, y,1)
        white_rects.remove((x,y))



    # time.sleep(0.3)
    pygame.display.update()





