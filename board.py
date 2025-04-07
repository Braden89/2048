import random
import math


class Board:
    def __init__(self):
        self.mWidth = 4
        self.mHeight = 4
        self.mBoard = [[0 for _ in range(4)] for _ in range(4)]

    def __str__(self):
        lines = []
        for row in self.mBoard:
            line = "|".join(f"{num:^5}" if num != 0 else "  .  " for num in row)
            lines.append(line)
        return "\n".join (lines)
    

    def setValue(self, collum, row, val):
        '''
        Sets value at given posisition to val. 
        if val or position is not valid, return -1, else, return 0
        '''

        # check if in bounds
        if collum >= self.mWidth or row >= self.mHeight:
            return -1
        
        # check if valid num (to be added)

        




    def addRandomValue(self):
        # sets a random value of a node that was 0 to 2 or 4
        # returns 0 if added returns -1 if could not add (all nodes full)
        possible_tiles = []
        found_tile = False
        for i in range(self.mWidth):
            for j in range(self.mHeight):
                if self.mBoard[i][j] == 0:
                    possible_tiles.append((i, j))
                    found_tile = True

        if found_tile == False:
            return -1
        else: 
            chosen_i, chosen_j = random.choice(possible_tiles)
            new_num = random.choice([2, 4])
            self.mBoard[chosen_i][chosen_j] = new_num

            return 0
        
    
    def moveUp(self):
        '''
        method for moving tiles upwards. 
        returns 0 if changes, -1 if none changed
        '''

        changed = False
        for collums in range(self.mWidth):
            collum = []
            has_num = False     # if has all 0, no need to do rest of collum
            for rows in range(self.mHeight):
                # get all values for collum
                collum.append(self.mBoard[rows][collums])
                if self.mBoard[rows][collums] != 0:
                    has_num = True

            # if it only found 0's, break
            if has_num == False:
                continue
            else: 
                pivot = 0
                last_num = 0
                # loop through the collum list and move any needed
                for i in range(len(collum)):

                    # if number is 0 or if is the first number in the row, skip
                    if collum[i] == 0 or i == 0:
                        # incase first number isnt 0, mark what is is
                        last_num = collum[i]
                        continue

                    # if it is not zero, but does not match the last number
                    elif collum[i] != last_num:
                        self.mBoard[pivot][collums] = collum[i]
                        pivot += 1
                        self.mBoard[i][collums] = 0
                        changed == True


                    # if not zero and matches last number, meaning it needs to combine
                    else:
                        # multiply last number by itself
                        self.mBoard[pivot - 1][collums] = last_num * 2

                        # set last_num to 0 to prevent matching multiple
                        last_num = 0
                        self.mBoard[i][collums] = 0
                        changed == True






                        

            
                

            





