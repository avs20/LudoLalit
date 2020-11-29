Ludo playing AI bot 


Rules of game
------------
1. Direction will be clockwise. 
2. Dice can take values 1-6 
3. Maximum of 4 players minimum of 4 players.
4. only on 6 player can get out of house 
5. Otherwise, only the out of the house goti can be move forward. 
6. There is no move backward.
7. Finish is at a particular step 
8. After that goti is out of the game. 
9. To check winner, check if all gotis are out of game 


4 Classes of these 
------

1. Ludo Board 
    4 players 


2. Players 
    
    
    methods 
    ------
    throwDice() - int value
    takeStep() - will move one goti

3. Dice 
    getValueAfter1Throw()- int value return

4. Goti 
    color
    id
    position- R-10,L-11
    stepsTaken
    move(numofSteps)




There should be some restricted moves also. 
Like if there is no availabe goti and you have a 6 then you should take 1 goti out of the house. 


