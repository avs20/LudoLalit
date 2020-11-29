from dice import Dice
from goti import Goti 
from player import Player 
from constants import * 
import time 
class Board:

    def __init__(self, names, color):
        self.players = []
        for name , color in zip(names, color):
            p1 = Player(name, color)
            self.players.append(p1)

    def printBoardState(self):
        for player in self.players:
            print(player.show_player_positions())

    def isGameOver(self):
        count = 0 
        for player in self.players:
            if player.isPlayerGameOver():
                count += 1

        return count > 2
    
    def startGame(self):
        '''
        game will run until 3 players gotis have been ended in the game. 


        '''
    
        while(not self.isGameOver()): 
            
            for player  in self.players:
                if not player.isPlayerGameOver():
                    pasa = player.throwDice()

                    # checks for 3 sixes 
                    if pasa == 6 :
                        pasa += player.throwDice()
                        if pasa == 12:
                            pasa += player.throwDice()
                            if pasa == 18:
                                pasa = 0 
                    
                    print(player.name,' got ', pasa)
                    goti_id = player.getRandomGotiId()

                    if goti_id is None and pasa> 6:
                        goti_id = player.getRandomFromInHouse()                       
                        pasa -= 6
                        player.moveGoti(goti_id,1)
                    elif goti_id is None and pasa < 6:
                        continue                   

                    player.moveGoti(goti_id, pasa)
                    # time.sleep(2)
            self.printBoardState()

                    
if __name__ == '__main__':
    
    players = ['Ashu', 'sbhubham', 'nitish', 'vikas']
    colors = ['blue','red','green','yellow']
    b = Board(players, colors)
    b.startGame()

    

