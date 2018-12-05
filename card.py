#########################################
# Player Class
#########################################
#########################################
#zpy_server.py Citation Comment:
#Lines 1-24: Original Code
#Lines 24-27: Adapted Code from 112 Sockets Website on Dots Game
#Lines 27-65: Original Code
#########################################

import random 
        
class Player(object):
    
    #Constructs Player Class
    def __init__(self, PID):
        self.PID = PID
        self.cards = []
        self.points = 0
        #player classifications
        self.isDictator = False
        self.isAlly = False
    
    #Adds Player PID
    def changePID(self, PID):
        self.PID = PID
    
    #Draws Card, adds to player deck
    def drawCard(self, data):
        cardNum = random.randint(0, len(data.cards)-1)
        card = data.cards[cardNum]
        self.cards.append(card)
        return card        
        
    #Plays Card, removes card
    def playCard(self, card):
        i = self.cards.index(card)
        self.cards.remove(card)
    
    #Adds Points based off round (single cards)
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
    
    #Adds Points based off round (pair cards)
    def addPointsPairs(self, data, pairs):
        addition = 0
        for pair in pairs:
            for card in pair:
                num = int(card[:-1])
                if num == 10 or num == 13:
                    addition += 10
                elif num == 5:
                    addition += 5
        self.points += addition
        return addition