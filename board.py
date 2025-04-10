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
    
    def getWidth(self):
        return self.mWidth
    
    def getHeight(self):
        return self.mHeight
    

    def setValue(self, row, collumn, val):
        '''
        Sets value at given posisition to val. 
        if val or position is not valid, return -1, else, return 0
        '''

        # check if in bounds
        # if collumn >= self.mWidth or row >= self.mHeight:
        #    print("setValue: Not within bounds")
        #    return -1
        # check if valid num using bitwise method.
        # binary_val = bin(val)
        # if (binary_val and (binary_val - 1) != 0) or (binary_val and binary_val - 1 != 0):
        #    print("setValue: Not a valid value")
        #    return -1
        self.mBoard[row][collumn] = val
        return 0
        
        

        





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
        for collumns in range(self.mWidth):
            col = []
            has_num = False     # if has all 0, no need to do rest of collumn
            for rows in range(self.mHeight):
                # get all values for collumn
                col.append(self.mBoard[rows][collumns])
                if col[rows] != 0:
                    has_num = True

            # if it only found 0's, go to next
            if has_num == False:
                continue
            else: 
                pivot = 0
                last_num = 0
                # loop through the collumn list and move any needed
                for i in range(len(col)):

                    # if number is 0 or if is the first number in the row, skip
                    if col[i] == 0 or i == 0:
                
                        #if first number not 0, increase pivot
                        if col[i] != 0:
                            pivot += 1
                            last_num = col[i]
                        continue

                    # if it is not zero, but does not match the last number
                    elif col[i] != last_num:
                        if i == pivot:
                            last_num = col[i]
                            pivot += 1

                        else:
                            self.mBoard[pivot][collumns] = col[i]
                            self.mBoard[i][collumns] = 0
                            last_num = col[i]
                            pivot += 1
                            changed = True


                    # if not zero and matches last number, meaning it needs to combine
                    else:
                        # multiply last number by 2
                        self.mBoard[pivot - 1][collumns] = last_num * 2

                        # set last_num to 0 to prevent matching multiple
                        last_num = 0
                        self.mBoard[i][collumns] = 0
                        changed = True
        return changed

    def moveLeft(self):
        '''
        method for moving tiles Left
        returns 0 if change happened, -1 if no change
        '''

        changed = False
        for rows in range(self.mHeight):
            row = []
            has_num = False

            # get all values from row
            for collumns in range(self.mWidth):
                row.append(self.mBoard[rows][collumns])
                if row[collumns] != 0:
                    has_num = True

            #if it only found 0's, go to next
            if has_num == False:
                continue
            else:
                pivot = 0
                last_num = 0
                # loop through the collumn list and ove any needed
                for i in range(len(row)):

                    # if number is 0 or is the first number in the row, skip
                    if row[i] == 0 or i == 0:
                        # if furst number not 0, increase pivot
                        if row[i] != 0:
                            pivot += 1
                            last_num = row[i]
                            
                        

                    # if it is not zero, but does not match the last number
                    elif row[i] != last_num:
                        if i == pivot:
                            last_num = row[i]
                            pivot += 1

                        
                        else:
                            self.mBoard[rows][pivot] = row[i]
                            self.mBoard[rows][i] = 0
                            last_num = row[i]
                            pivot += 1
                            changed = True

                    # if not zero and matches last number, meaning it needs to combine
                    else:
                        # multiply number by 2
                        self.mBoard[rows][pivot - 1] = last_num * 2

                        #set last_num to 0 to prevent matching multiple
                        last_num = 0
                        self.mBoard[rows][i] = 0
                        changed = True
        return changed


    def moveDown(self):
        '''
        method for moving tiles down. returns True if changed, False if no change
        '''
        changed = False
        for collumns in range(self.mWidth):
            col = []
            has_num = False
            for rows in range(self.mHeight):
                # get all values for collumn
                col.append(self.mBoard[rows][collumns])
                if self.mBoard[rows][collumns] != 0:
                    has_num = True

            #if only found 0's, skip to next
            if has_num == False:
                continue
            else:
                pivot = self.mHeight - 1
                last_num = 0
                col.reverse()

                # loop through the collumn list and move any if needed
                for i in range(len(col)):
                    offset = self.mHeight - i - 1
                    
                        
                    # if first number is 0 or if it is the first number in the collumn, skip
                    if col[i] == 0 or i == 0:

                        # if number is not 0, decrease pivot
                        if col[i] != 0:
                            pivot -= 1
                            last_num = col[i]
                        continue

                    # if it is not zero, but does not match the last number
                    elif col[i] != last_num:
                        if offset == pivot:
                            last_num = col[i]
                            pivot -= 1

                        else:
                            self.mBoard[pivot][collumns] = col[i]
                            self.mBoard[offset][collumns] = 0
                            last_num = col[i]
                            pivot -= 1
                            changed = True

                    # if not zero and matches last number, meaning it needs to combine
                    else:
                        # multiply last number by 2
                        self.mBoard[pivot + 1][collumns] = last_num * 2

                        # set last_num to 0 to prevent matching multiple
                        last_num = 0
                        self.mBoard[offset][collumns] = 0
                        changed = True

        return changed


    def moveRight(self):
        '''
        method for moving tiles down. returns True if changed, False if no change
        '''
        changed = False
        for rows in range(self.mHeight):
            row = []
            has_num = False
            for collumns in range(self.mHeight):
                # get all values for collumn
                row.append(self.mBoard[rows][collumns])
                if self.mBoard[rows][collumns] != 0:
                    has_num = True

            #if only found 0's, skip to next
            if has_num == False:
                continue
            else:
                pivot = self.mHeight - 1
                last_num = 0
                row.reverse()

                # loop through the collumn list and move any if needed
                for i in range(len(row)):
                    offset = self.mWidth - i - 1
                    
                        
                    # if first number is 0 or if it is the first number in the collumn, skip
                    if row[i] == 0 or i == 0:

                        # if number is not 0, decrease pivot
                        if row[i] != 0:
                            pivot -= 1
                            last_num = row[i]
                        continue

                    # if it is not zero, but does not match the last number
                    elif row[i] != last_num:
                        if offset == pivot:
                            last_num = row[i]
                            pivot -= 1

                        else:
                            self.mBoard[rows][pivot] = row[i]
                            self.mBoard[rows][offset] = 0
                            last_num = row[i]
                            pivot -= 1
                            changed = True

                    # if not zero and matches last number, meaning it needs to combine
                    else:
                        # multiply last number by 2
                        self.mBoard[rows][pivot + 1] = last_num * 2

                        # set last_num to 0 to prevent matching multiple
                        last_num = 0
                        self.mBoard[rows][offset] = 0
                        changed = True

        return changed

                        

            
                

            





