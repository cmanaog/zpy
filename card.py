##########################
# Player Class
##########################
import random 
        
class Player(object):
    
    def __init__(self, PID):
        self.PID = PID
        self.cards = []
        #self.isDictator = False
        
    def changePID(self, PID):
        self.PID = PID
        
    def drawCard(self, deck):
        cardNum = random.randint(0, len(deck))
        card = deck[cardNum]
        self.cards.append(card)
        deck.remove(card)
        return card
    



