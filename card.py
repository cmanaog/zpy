##########################
# Player Class
##########################
import random 
        
class Player(object):
    
    def __init__(self, PID):
        self.PID = PID
        self.cards = []
        self.points = 0
        #self.isDictator = False
        
    def changePID(self, PID):
        self.PID = PID
    
    def drawCard(self, data):
        cardNum = random.randint(0, len(data.cards)-1)
        print("card to remove", cardNum)
        #print(data.cards)
        card = data.cards[cardNum]
        self.cards.append(card)
        #data.cards.remove(card)
        return card        
        
    def playCard(self, card):
        self.cards.remove(card)
    



