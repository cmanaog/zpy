##########################
# Player Class
##########################
import random 
        
class Player(object):
    
    def __init__(self, PID):
        self.PID = PID
        self.cards = []
        self.cardPos = []
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
        i = self.cards.index(card)
        self.cards.remove(card)
        self.cardPos.pop(i)
    
    def addPoints(self, data):
        total = 0
        for card in data.roundCards:
            num = int(card[:-1])
            addition = 0
            if num == 10 or num == 13:
                addition += 10
            elif num == 5:
                addition += 5
            total += addition
        self.points += total
        return total
            
    def cardPositions(self, data):
        x,y = data.width/2 - 6 * data.margin, data.height - 5 * data.margin
        for card in data.me.cards:
            #print(x,y)
            if x >= data.width/2 + 5 * data.margin:
                x = data.width/2 - 6 * data.margin
                y = data.height - 3 * data.margin
            self.cardPos.append([x,y])
            x += data.margin
        print(self.cardPos)



