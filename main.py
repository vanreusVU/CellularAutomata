from math import ceil, floor
import sys
from typing import List, Tuple
import pygame
from cell import Cell
from color_constants import Color
import global_ as glb
from utilities import Point

# Initalize


class CellularAutomata:
    def __init__(self) -> None:
        glb.initGlobal()

        glb.WIDTH = 720
        glb.HEIGHT = 720 
        glb.BLOCKSIZE = 10 
        glb.SIZE = glb.WIDTH, glb.HEIGHT

        glb.SCREEN = pygame.display.set_mode(glb.SIZE)
        glb.CLOCK = pygame.time.Clock()

        pygame.init()

        self.cells = []
        
        self.begin()
        pass

    def begin(self) -> None:
        while True:
            glb.SCREEN.fill(Color.BLACK)
            #self.drawGrid()

            # Type cast
            cell : Cell

            # Apply Rules
            for cell in self.cells:
                cell.applyRule(self.cells)

            # Draw
            for cell in self.cells:
                block_loc = (cell.loc[0] * glb.BLOCKSIZE), (cell.loc[1] * glb.BLOCKSIZE) 
                temp_rect = pygame.Rect(block_loc, (glb.BLOCKSIZE,glb.BLOCKSIZE))
                pygame.draw.rect(glb.SCREEN, cell.color, temp_rect)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:     
                    self.spawnCell(pygame.mouse.get_pos())
                if event.type == pygame.QUIT:
                    sys.exit()
                
            pygame.display.flip()
            glb.CLOCK.tick(60)
            

    def spawnCell(self, mouse_pos : Point) -> bool:
        block_pos = self.getBlockFromPos(mouse_pos)
      
        # block_loc = ((block_pos[0] * glb.BLOCKSIZE)), ((block_pos[1] * glb.BLOCKSIZE) )
        self.cells.append(Cell(block_pos, 0))
        return True

    def drawGrid(self) -> None:
        for x in range(glb.WIDTH):
            for y in range(glb.HEIGHT):
                rect = pygame.Rect(x*glb.BLOCKSIZE, y*glb.BLOCKSIZE,glb.BLOCKSIZE, glb.BLOCKSIZE)
                pygame.draw.rect(glb.SCREEN, Color.DARKGRAY, rect, 1)       

    def getBlockFromPos(self, mouse_pos : Point) -> Point:
        block_x = floor(mouse_pos[0] / glb.BLOCKSIZE)
        block_y = floor(mouse_pos[1] / glb.BLOCKSIZE)
        
        return Point(block_x, block_y)

if __name__ == "__main__":
    CellularAutomata()