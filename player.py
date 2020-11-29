from dice import Dice
from goti import Goti
from constants import * 
import random


class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.dice = Dice()
        self.goti1 = Goti(color, 1, [board_map[color], 14])
        self.goti2 = Goti(color, 2, [board_map[color], 14])
        self.goti3 = Goti(color, 3, [board_map[color], 14])
        self.goti4 = Goti(color, 4, [board_map[color], 14])
        self.gotimap = {1 : self.goti1, 2 : self.goti2, 3: self.goti3, 4:self.goti4}


    def throwDice(self):
        return self.dice.getValueAfter1Throw()

    def moveGoti(self, id, numSteps):
        toMove = self.gotimap[id]
        toMove.move(numSteps)

    def show_player_positions(self):
        print('Printing current state for ', self.name)
        print(self.goti1.getCurrentPos())
        print(self.goti2.getCurrentPos())
        print(self.goti3.getCurrentPos())
        print(self.goti4.getCurrentPos())
    
    def isPlayerGameOver(self):
        count = 0 
        for id in self.gotimap:
            if self.gotimap[id].checkIfWon():
                count += 1
        
        return count == 4

    def getRandomGotiId(self):
        '''
        This will return a random goti which is out of the house 
        and can be moved. 
        TODO to be replace later with option from the player
        '''
        avaiable_gotis = []
        for id in self.gotimap:
            if self.gotimap[id].checkIfOutHouse() and not self.gotimap[id].checkIfWon():
                avaiable_gotis.append(id)

        if len(avaiable_gotis) == 0:
            return None
        return random.choice(avaiable_gotis)

    def getRandomFromInHouse(self):
        '''
        returns a random goti which is inside the house
        '''
        choices = []
        for id in self.gotimap:
            if self.gotimap[id].position is None:
                choices.append(id)
        return random.choice(choices)



            
if __name__ == '__main__':
    p1 = Player('ashu', 'blue')

    outOfHouse = False
    for i in range(10):
        num = p1.throwDice()
        if outOfHouse:
        
            print('The dice got ', num)
            p1.moveGoti(1, num)
            p1.show_player_positions()
        if not outOfHouse and num == 6:
            outOfHouse = True
            p1.moveGoti(1, 1)
            continue
        

