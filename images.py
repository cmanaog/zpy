import random
import math
from tkinter import *
import copy
from card import *
from image_util import *

from PIL import Image
from resizeimage import resizeimage
'''data.cards = [(14,"s"), (14, "c"), (14, "d"),(14, "h"),\
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
data.sleekbg = Image.open('img/sleekbg.gif')
data.sleekbg = data.sleekbg.resize((1000,700))
data.sleekbg.save("img/sleekbg.gif")
'''

'''#starting
startX = data.width/2 - 6.5 * data.margin
startY_1 = data.height - 5 * data.margin - data.cardHeight/2 
startY_2 = data.height - 3 * data.margin - data.cardHeight/2 
#card dimensions
cardWidth = data.margin
cardHeight = 73
#ending dimensions

#endX = startX + data.startingHand // 2 * cardWidth
endY_1 = startY_1 + cardHeight
endY_2 = startY_2 + cardHeight
print("setup")
#check if within range:
for i in range(len(data.me.cards)):
    endX = startX + cardWidth
    if i < data.startingHand // 2:
        print("first")
        if x >= startX and x <= endX and y >= startY_1 and y <= endY_1:
            return data.me.cards[i]
    else:
        print("second")
        if x >= startX and x <= endX and y >= startY_2 and y <= endY_2:
            return data.me.cards[i]
    startX = endX
print("out")
return None'''