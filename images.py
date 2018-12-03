import random
import math
from tkinter import *
import copy
from card import *

from PIL import Image
from resizeimage import resizeimage
cards = [(14,"s"), (14, "c"), (14, "d"),(14, "h"),\
(2,"s"), (2, "c"), (2, "d"),(2, "h"),\
(3,"s"), (3, "c"), (3, "d"), (3, "h"),\
(4,"s"), (4, "c"), (4, "d"), (4, "h"),\
(5,"s"), (5, "c"), (5, "d"), (5, "h"),\
(6,"s"), (6, "c"), (6, "d"), (6, "h"),\
(7,"s"), (7, "c"), (7, "d"), (7, "h"),\
(8,"s"), (8, "c"), (8, "d"), (8, "h"),\
(9,"s"), (9, "c"), (9, "d"), (9, "h"),\
(10,"s"), (10, "c"), (10, "d"), (10, "h"),\
(11,"s"), (11, "c"), (11, "d"), (11, "h"),\
(12,"s"), (12, "c"), (11, "d"), (11, "h"),\
(13,"s"), (13, "c"), (13, "d"), (13, "h")]
img = Image.open('img/Cards/11h.gif')
img = img.resize((50,73))
img.save("img/Cards/11h.gif")


trumpNum = "2"
trumpSuit = "s"
cards = ["2s", "3s", "4s", "4h"]
def isValid(roundCards, card):
    
    startHand = roundCards[0]
    startSuit = startHand[-1] #first suit
    if startHand[:-1] == trumpNum:
        startSuit = trumpSuit
    
    #following suit, start suit is not trump suit
    if card[-1] == startSuit and startSuit != trumpSuit and card[:-1] != str(trumpNum):
        return True
    
    
    
    #following suit, starting suit is trump suit
    elif startSuit == trumpSuit and (card[-1] != trumpSuit and card[:-1] != str(trumpNum)):
        return False
    
    #add case where does not have suit
    else:
        if startSuit != trumpSuit:
            for c in cards:
                if startSuit in c and c[:-1] != str(data.trumpNum):
                    return False
        else:
            for c in cards:
                if startSuit in c or c[:-1] == str(data.trumpNum):
                    return False
    return True

