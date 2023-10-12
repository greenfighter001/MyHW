import pygame
import sys
from game_map import GameMap
from game_timer import GameTimer

BG = (245, 245, 245)
lineColor = (255, 255, 255)
aliveColor = (106, 90, 205)
deadColor = (230,230,250)

interval = 0.4
size = 640, 640
border = 20
lineLength = size[0]-border*2

class UI:
    def __init__(self, map:GameMap):
        count = 0
        self.gridNumber = map.Col
        self.cellLength = lineLength / self.gridNumber
        pygame.init()
        timer = GameTimer(0.02)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Game of Life")
        timer.start()
        while True:
            count += 1
            if count>=500*interval:
                count = 0
                map.update(map.Row, map.Col)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if border<pos[0]<=size[0]-border and border<pos[1]<=size[1]-border:
                        x = int((pos[0]-border)/self.cellLength)
                        y = int((pos[1] - border) / self.cellLength)
                        if map.map[x][y]==True:
                            map.set(x, y, False)
                        else:
                            map.set(x, y, True)
            self.screen.fill(BG)
            self.drawLine(map)
            pygame.display.update()

    def drawLine(self, map):
        for i in range(self.gridNumber):
            for j in range(self.gridNumber):
                if map.get(i, j)==True:
                    color = aliveColor
                else:
                    color = deadColor
                pygame.draw.rect(self.screen, color,
                                 (border+i*self.cellLength, border+j*self.cellLength,
                                  self.cellLength, self.cellLength))
        for i in range(self.gridNumber+1):
            pygame.draw.line(self.screen, lineColor,
                             (border+i*self.cellLength, border),
                             (border+i*self.cellLength, border+lineLength))
            pygame.draw.line(self.screen, lineColor,
                             (border, border + i * self.cellLength),
                             (border+lineLength, border + i * self.cellLength))
