import numpy as np


def step(Field):
    '''
    Field - class of Field
    
    Method generate new field by basics rules
    '''
    pole = Field.cells.copy()
    for x in range(1, pole.size_x - 1, 1): # FixMe Now program doesn't work with borders
        for y in range(1, pole.size_y - 1, 1):
            # counting number of neighbors
            neighbors = 0
            if pole[x + 1][y].live:
                neighbors += 1
            if pole[x - 1][y].live:
                neighbors += 1
            if pole[x][y + 1].live:
                neighbors += 1
            if pole[x][y - 1].live:
                neighbors += 1
            # checking future for cell
            if pole[x][y].live > 0:
                if neighbors < 2 or neighbors == 4:
                    pole[x][y].live -= 1
            else:
                if neighbors == 3:
                    pole[x][y].live += 1
    Field.cells = pole.copy()
            
            
            
if __name__ == "__main__":
    print("This module is not for direct call!")

        
            