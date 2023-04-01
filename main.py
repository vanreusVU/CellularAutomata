from math import ceil, floor
import sys
from typing import List, Tuple
import pygame
from cell import Cell
from color_constants import Color
import global_ as glb
from utilities import Point

# Initalize
WIDTH = 720
HEIGHT = 720 
BLOCKSIZE = 10 
SIZE = WIDTH, HEIGHT

SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()


class CellularAutomata:
    def __init__(self) -> None:
        pygame.init()
        self.cells = [[0] * WIDTH/BLOCKSIZE for _ in range(HEIGHT/BLOCKSIZE)] 
        self.begin()

    def begin(self) -> None:
        while True:
            # Paint the screen to @Color
            SCREEN.fill(Color.BLACK)

            # Type cast
            cell : Cell

            # Apply Rules
            for cell in self.cells:
                cell.applyRule(self.cells)

            # Draw
            '''for cell in self.cells:
                block_loc = (cell.loc[0] * BLOCKSIZE), (cell.loc[1] * BLOCKSIZE) 
                temp_rect = pygame.Rect(block_loc, (BLOCKSIZE,BLOCKSIZE))
                pygame.draw.rect(SCREEN, cell.color, temp_rect)
            '''

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:     
                    print("Mouse Button pressed")
                    #self.spawnCell(pygame.mouse.get_pos())
                elif event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            pygame.display.flip()
            CLOCK.tick(60)
            
    def spawnCell(self, mouse_pos : Point) -> bool:
        block_pos = self.getBlockFromPos(mouse_pos)
      
        # block_loc = ((block_pos[0] * BLOCKSIZE)), ((block_pos[1] * BLOCKSIZE) )
        self.cells.append(Cell(block_pos, 0))
        return True     

    def getBlockFromPos(self, mouse_pos : Point) -> Point:
        block_x = floor(mouse_pos[0] / BLOCKSIZE)
        block_y = floor(mouse_pos[1] / BLOCKSIZE)
        
        return Point(block_x, block_y)

if __name__ == "__main__":
    CellularAutomata()