import random 
class Dice:
    def __init__(self):
        print('The Game Starts now!')
    
    def getValueAfter1Throw(self):
        return random.randint(1,6)
    
if __name__ == '__main__':
    d = Dice()
    for i in range(50):
        print(d.getValueAfter1Throw())
        
    
