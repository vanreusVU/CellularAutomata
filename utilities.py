# Default Modules
from enum import Enum
from typing import List, Tuple
import operator
import random

class Point(tuple): 
    def __new__(self, x, y):
        return tuple.__new__(Point, (x, y)) 

    def __str__(self) -> str:
        return f"(X: {self[0]}, Y: {self[1]})"

    def __add__(self, __o : object):
        return Point(self[0] + __o[0], self[1] + __o[1])

    def __sub__(self, __o : object):
        return Point(self[0] - __o[0], self[1] - __o[1])

    def __eq__(self, __o: object) -> bool:
        return __o[0] == self[0] and __o[1] == self[1]

    def __ne__(self, __o: object) -> bool:
        return __o[0] != self[0] or __o[1] != self[1]

def getPercentage(number, percentage) -> float:
        '''returns the x% of the number

        :param number: number to take the percentage of
        :type number: any numeric type
        :param percentage: percentage to be taken (0-100)
        :type percentage: any numeric type
        :return: floored percentage
        :rtype: float
        '''        
        return (number/100)*percentage

def percentageDifference(number1, number2):
    '''
    Percentage difference between number1 and number2
    - means number2 is that percent less than number1

    :param number1: number1 to compare
    :type number1: any numeric type
    :param number2: number to be compared
    :type number2: any numeric type
    :return: percentage difference between number1 and number2
    :rtype: float
    '''    

    # If one of the numbers is 0 then we need to increase both of the numbers so that the
    # difference is the same but no 0 exists. !!Division by 0 is not possible!!
    while number1 == 0 or number2 == 0:
        number1 += 1
        number2 += 1

    return ((number2 - number1) / (number1)) * 100

class MinMax():
    ''' Simple class that holds two variables under the name of MIN and MAX.'''

    def __init__(self, min, max) -> None:
        '''Defines min and max variables'''
        self.MIN = min
        self.MAX = max
        pass

    def __str__(self) -> str:
        return f"MIN: {self.MIN}, MAX: {self.MAX}"


def isWithinBounds(location : Point, tiles) -> bool:
    '''
    Checks if the given location is within the bounds of the tiles

    :param location: location to check
    :type location: Coordinate
    :param tiles: 2D matrix to check the bounds for 
    :type tiles: List[List[]]
    :return: weather the location is within the bounds of the matrix
    :retval True: location within bounds
    :retval False: location is out of bounds
    :rtype: bool
    '''    
    
    return (location[0] >= 0 and location[0] < len(tiles)) and (location[0] >= 0 and location[0] < len(tiles[0]))  