class Goti:
    def __init__(self, color, id, startPos):
        super().__init__()
        self.color = color
        self.id = id
        self.position = None
        self.stepsTaken = None
        self.startPos = startPos
        
    def getCurrentPos(self):
        return self.position, self.stepsTaken

    def checkIfOutHouse(self):
        '''
        checks if the goti can be moved or not
        '''
        return self.position is not None

      

    def __move__(self, numSteps):
        '''
        moves the goti to the next step
        '''
        if self.stepsTaken is None and numSteps > 1:
            print('Invalid move')
            return -1

        if self.stepsTaken is None and numSteps == 1:
            self.stepsTaken = 0
            #need to set the position also
            self.position = self.startPos
            return 0
        if self.position[0] == 'H':
            print('Invalid move, can\'t move this goti')
            return -1 

        if self.stepsTaken is not None and self.position:
            '''
            18 ke baad 0 aayega 
            6-7-13 # of steps < 50
            6-7-8 # number of steps >=50 
            TRDL
            (R, )
            '''
            dir_dict = {'T' : 'R',
             'R' : 'D',
             'D' : 'L',
             'L' : 'T'   }

            
            # check current position 
            if self.position[1]  + numSteps <= 7:
                self.position[1] += numSteps
                self.stepsTaken += numSteps
            else:
                # we have to check for home run or normal run 
                if self.stepsTaken + numSteps > 50 :
                    if (self.stepsTaken + numSteps)  > 57:
                        print('Invalid Move')
                        return  -1 
                    self.position[1] = self.position[1] + numSteps
                    self.stepsTaken += numSteps

                elif self.position[1] + numSteps >18:
                    self.position[0] = dir_dict[self.position[0]]
                    self.position[1] = (self.position[1] + numSteps) % 18
                    self.stepsTaken += numSteps
                else:
                    self.position[1] = self.position[1] + numSteps + 5
                    self.stepsTaken += numSteps

    def move(self,numSteps):
        while (numSteps // 6 > 1):
            result = self.__move__(6)

            if result :
                return -1,numSteps # the move was invalid, move other goti 
            else:
                numSteps = numSteps - 6
                if self.checkIfWon():
                    return 1, numSteps # this goti is finished. move another goti. 
            
            return 0,0   # all things normal, take another chance
            
            

        self.__move__(numSteps)

    def checkIfWon(self):
        if self.stepsTaken == 57:
            self.stepsTaken = -1 
            self.position = ['H',0]
            return True
        return False


           
if __name__ == '__main__':
    g = Goti('blue',1,['T',14])

    print(g.getCurrentPos())
    #inside and move 8 steps
    g.move(8)
    # inside and move 1 step 
    g.move(1)
    print(g.getCurrentPos())

    g.move(12)
    print(g.getCurrentPos())

    g.move(30)
    print(g.getCurrentPos())

    g.move(15)
    print(g.getCurrentPos())





            

