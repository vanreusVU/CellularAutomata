import random
from typing import Tuple
from color_constants import Color
from utilities import Point
import global_ as glb 

class Cell():
    def __init__(self, loc : Point, type : int) -> None:
        self.loc = loc
        self.color = Color.AQUA
        self.type = type
        return

    def applyRule(self, cells):
        # Vertical
        if self.isWithinBounds(cells, self.loc + (0,1)):
            if not self.isOverlaping(cells,(0,1)):
                self.loc += (0,1)
                print(self.loc)
                return

        pass

    def isWithinBounds(self, cells : Point, loc):
        return (loc[0] >= 0 and loc[0] < glb.WIDTH) and (loc[1] >= 0 and loc[1] < glb.HEIGHT)

    def isOverlaping(self, cells, check_loc : Point) -> bool:
        for cell
        if cells[self.loc[1] + check_loc[1]][self.loc[0] + check_loc[0]] != None:
            return True

        return False
