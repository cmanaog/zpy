
#############################
# ZPY
#############################

import socket
import threading
from queue import Queue

HOST = "" # put your IP address here if playing on multiple computers, everyone else adds that IP addresss and port. sometimes, using localhost will help
PORT = 49185 #change each time you run, all computers use same host and port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((HOST,PORT))
print("connected to server")

#client's personal mailbox
def handleServerMsg(server, serverMsg):
  server.setblocking(1)
  msg = ""
  command = ""
  while True:
    msg += server.recv(10).decode("UTF-8") #takes incoming msgs
    command = msg.split("\n")
    while (len(command) > 1):
      readyMsg = command[0]
      msg = "\n".join(command[1:])
      serverMsg.put(readyMsg) #puts msgs in msg queue, later translated to timer fired
      command = msg.split("\n")

# Above Code from 15-112 website on Sockets
# Barebones timer, mouse, and keyboard events

import random
import string
import math
from tkinter import *
import copy
from images import *
from card import *
#from image_util import *

from PIL import Image
from resizeimage import resizeimage
'''img = Image.open('img/Cards/11h.gif')
img = img.resize((50,73))
img.save("img/Cards/11h.gif")'''

####################################
# init
####################################

#Initializes Data
def init(data):
    # Game Mode
    data.mode = "start"
    data.margin = 50
    
    #data.me = Dot("Lonely", data.width/2, data.height/2)
    #data.otherStrangers = dict()
    
    data.me = Player("Lonely")
    data.others = dict()
    
    data.startbg = PhotoImage(file="img/startbg.gif")
    data.sleekbg = PhotoImage(file="img/sleekbg.gif")
    
    #"s" -> Spade, "c" -> Clover, "d" -> Diamond, "h" -> Heart
    data.cards = ["14s", "14c", "14d", "14h",\
    "2s", "2c", "2d", "2h",\
    "3s", "3c", "3d", "3h",\
    "4s", "4c", "4d", "4h",\
    "5s", "5c", "5d", "5h",\
    "6s", "6c", "6d", "6h",\
    "7s", "7c", "7d", "7h",\
    "8s", "8c", "8d", "8h",\
    "9s", "9c", "9d", "9h",\
    "10s", "10c", "10d", "10h",\
    "11s", "11c", "11d", "11h",\
    "12s", "12c", "12d", "12h",\
    "13s", "13c", "13d", "13h",\
    "14s", "14c", "14d", "14h",\
    "2s", "2c", "2d", "2h",\
    "3s", "3c", "3d", "3h",\
    "4s", "4c", "4d", "4h",\
    "5s", "5c", "5d", "5h",\
    "6s", "6c", "6d", "6h",\
    "7s", "7c", "7d", "7h",\
    "8s", "8c", "8d", "8h",\
    "9s", "9c", "9d", "9h",\
    "10s", "10c", "10d", "10h",\
    "11s", "11c", "11d", "11h",\
    "12s", "12c", "12d", "12h",\
    "13s", "13c", "13d", "13h"]
    #data.cards = ["1s", "1c", "1d", "1h",\
    #"2s", "2c", "2d", "2h"]
    
    cardsImg = {
        "14c": PhotoImage(file="img/Cards/14c.gif"),
        "14d": PhotoImage(file="img/Cards/14d.gif"),
        "14h": PhotoImage(file="img/Cards/14h.gif"),
        "14s": PhotoImage(file="img/Cards/14s.gif"),
        "13c": PhotoImage(file="img/Cards/13c.gif"),
        "13d": PhotoImage(file="img/Cards/13d.gif"),
        "13h": PhotoImage(file="img/Cards/13h.gif"),
        "13s": PhotoImage(file="img/Cards/13s.gif"),
        "12c": PhotoImage(file="img/Cards/12c.gif"),
        "12d": PhotoImage(file="img/Cards/12d.gif"),
        "12h": PhotoImage(file="img/Cards/12h.gif"),
        "12s": PhotoImage(file="img/Cards/12s.gif"),
        "11c": PhotoImage(file="img/Cards/11c.gif"),
        "11d": PhotoImage(file="img/Cards/11d.gif"),
        "11h": PhotoImage(file="img/Cards/11h.gif"),
        "11s": PhotoImage(file="img/Cards/11s.gif"),
        "10c": PhotoImage(file="img/Cards/10c.gif"),
        "10d": PhotoImage(file="img/Cards/10d.gif"),
        "10h": PhotoImage(file="img/Cards/10h.gif"),
        "10s": PhotoImage(file="img/Cards/10s.gif"),
        "9c": PhotoImage(file="img/Cards/9c.gif"),
        "9d": PhotoImage(file="img/Cards/9d.gif"),
        "9h": PhotoImage(file="img/Cards/9h.gif"),
        "9s": PhotoImage(file="img/Cards/9s.gif"),
        "8c": PhotoImage(file="img/Cards/8c.gif"),
        "8d": PhotoImage(file="img/Cards/8d.gif"),
        "8h": PhotoImage(file="img/Cards/8h.gif"),
        "8s": PhotoImage(file="img/Cards/8s.gif"),
        "7c": PhotoImage(file="img/Cards/7c.gif"),
        "7d": PhotoImage(file="img/Cards/7d.gif"),
        "7h": PhotoImage(file="img/Cards/7h.gif"),
        "7s": PhotoImage(file="img/Cards/7s.gif"),
        "6c": PhotoImage(file="img/Cards/6c.gif"),
        "6d": PhotoImage(file="img/Cards/6d.gif"),
        "6h": PhotoImage(file="img/Cards/6h.gif"),
        "6s": PhotoImage(file="img/Cards/6s.gif"),
        "5c": PhotoImage(file="img/Cards/5c.gif"),
        "5d": PhotoImage(file="img/Cards/5d.gif"),
        "5h": PhotoImage(file="img/Cards/5h.gif"),
        "5s": PhotoImage(file="img/Cards/5s.gif"),
        "4c": PhotoImage(file="img/Cards/4c.gif"),
        "4d": PhotoImage(file="img/Cards/4d.gif"),
        "4h": PhotoImage(file="img/Cards/4h.gif"),
        "4s": PhotoImage(file="img/Cards/4s.gif"),
        "3c": PhotoImage(file="img/Cards/3c.gif"),
        "3d": PhotoImage(file="img/Cards/3d.gif"),
        "3h": PhotoImage(file="img/Cards/3h.gif"),
        "3s": PhotoImage(file="img/Cards/3s.gif"),
        "2c": PhotoImage(file="img/Cards/2c.gif"),
        "2d": PhotoImage(file="img/Cards/2d.gif"),
        "2h": PhotoImage(file="img/Cards/2h.gif"),
        "2s": PhotoImage(file="img/Cards/2s.gif")
    
    }
    data.cardsImg = cardsImg
    data.cardHeight = 73
    
    data.roundCards = []
    data.startSuit = ""
    
    data.turn = "Player1"
    data.dictator = None
    data.ally = ""
    
    data.startingPlayer = ""
    
    data.allyCardAppear = None
    data.allyCard = ""
    #data.allyCardOccur = 0
    
    data.trumpSuit = None
    data.trumpNum = 2
    
    data.distribute = False
    
    #opposition 
    data.startingHand = 24
    data.points = 0
    
    #numebr of players that have gone in a round 
    data.numPlayed = 0
    
    #dictator Swaps
    data.clickedPot = False
    data.potCard = None
    data.clickedHand = False
    data.handCard = None
    data.swap = False
    
    #winning
    data.whoWon = ""
    
####################################
# mode dispatcher
####################################

#Calls appropriate function for mouse press based on mode
def mousePressed(event, data):
    if (data.mode == "start"): startMousePressed(event, data)
    elif (data.mode == "playGame"):   playGameMousePressed(event, data)
    elif (data.mode == "end"):       endMousePressed(event, data)
    elif (data.mode == "options"):       optionsMousePressed(event, data)
    elif (data.mode == "rules"):       rulesMousePressed(event, data)
    elif (data.mode == "setup"):       setupMousePressed(event, data)
    elif (data.mode == "dictator"):       dictMousePressed(event, data)

#Calls appropriate function for key press based on mode
def keyPressed(event, data):
    #Calls appropriate function for mouse press based on mode
    if (data.mode == "start"): startKeyPressed(event, data)
    elif (data.mode == "playGame"):   playGameKeyPressed(event, data)
    elif (data.mode == "end"):       endKeyPressed(event, data)
    elif (data.mode == "options"):       optionsKeyPressed(event, data)
    elif (data.mode == "rules"):       rulesKeyPressed(event, data)
    elif (data.mode == "setup"):       setupKeyPressed(event, data)
    elif (data.mode == "dictator"):       dictKeyPressed(event, data)
    
#Calls appropriate function for time based on mode
def timerFired(data):
    if (data.mode == "start"): startTimerFired(data)
    elif (data.mode == "playGame"):   playGameTimerFired(data)
    elif (data.mode == "end"):       endTimerFired(data)
    elif (data.mode == "options"):       optionsTimerFired(data)
    elif (data.mode == "rules"):       rulesTimerFired(data)
    elif (data.mode == "setup"):       setupTimerFired(data)
    elif (data.mode == "dictator"):       dictTimerFired(data)
    
#Calls appropriate function for drawing based on mode
def redrawAll(canvas, data):
    if (data.mode == "start"): startRedrawAll(canvas, data)
    elif (data.mode == "playGame"):   playGameRedrawAll(canvas, data)
    elif (data.mode == "end"):       endRedrawAll(canvas, data)
    elif (data.mode == "options"):       optionsRedrawAll(canvas, data)
    elif (data.mode == "rules"):       rulesRedrawAll(canvas, data)
    elif (data.mode == "setup"):       setupRedrawAll(canvas, data)
    elif (data.mode == "dictator"):       dictRedrawAll(canvas, data)
    
####################################
# start mode
####################################
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)
    
def startMousePressed(event, data):
    if (event.x > data.width/2 - 3 * data.margin and event.x < data.width/2 + 3 * data.margin and event.y > data.height/2 - data.margin and event.y < data.height/2):
        data.mode = "setup"
    elif (event.x > data.width/2 - 3 * data.margin and event.x < data.width/2 + 3 * data.margin and event.y > data.height/2 + data.margin and event.y < data.height/2 + 2 * data.margin):
        data.mode = "options"
    elif(event.x > data.width/2 - 3 * data.margin and event.x < data.width/2 + 3 * data.margin and event.y > data.height/2 + 3 * data.margin and event.y < data.height/2 + 4 * data.margin):
        data.mode = "rules"

#switches to game mode
def startKeyPressed(event, data):
    if (event.keysym == "p"):
        data.mode = "playGame"

#incrememnts moving block based off time 
def startTimerFired(data):
    pass

#Draws block and text
def startRedrawAll(canvas, data):
    canvas.create_image(0,0,anchor=NW, image=data.startbg)
    canvas.create_text(data.width/2, data.height/4,
                       text="Zhao Peng You", font="Papyrus 100 bold")
           
    #Start Screen
    canvas.create_rectangle(data.width/2 - 3 * data.margin, data.height/2 - data.margin, data.width/2 + 3 * data.margin, data.height/2, fill = "red")
    canvas.create_text(data.width/2, data.height/2 - data.margin/2,
                       text="Start", font="Papyrus 20")
    
    #Options Screen
    canvas.create_rectangle(data.width/2 - 3 * data.margin, data.height/2 + data.margin, data.width/2 + 3 * data.margin, data.height/2 + 2 * data.margin, fill = "red")
    canvas.create_text(data.width/2, data.height/2 + 3 * data.margin/2,
                       text="Options", font="Papyrus 20")
    
    #Rules Screen
    canvas.create_rectangle(data.width/2 - 3 * data.margin, data.height/2 + 3 * data.margin, data.width/2 + 3 * data.margin, data.height/2 + 4 * data.margin, fill = "red")
    canvas.create_text(data.width/2, data.height/2 + 7 * data.margin/2,
                       text="Rules", font="Papyrus 20")
####################################
# options mode
####################################

def optionsMousePressed(event, data):
    if (event.x > data.margin and event.x < data.margin * 3 and event.y > data.margin and event.y < data.margin * 2):
        data.mode = "start"

#switches to game mode
def optionsKeyPressed(event, data):
    pass

#incrememnts moving block based off time 
def optionsTimerFired(data):
    pass
   
#Draws block and text
def optionsRedrawAll(canvas, data):
    canvas.create_image(0,0,anchor=NW, image=data.startbg)
    canvas.create_rectangle(data.margin, data.margin, data.margin * 3, data.margin * 2, fill = "blue")
    canvas.create_text(data.margin * 2, data.margin * 1.5, text = "Home", font = "Papyrus 20")
    canvas.create_text(data.width/2, data.height/4 - data.margin * 2,
                       text="Options", font="Papyrus 50 bold")
                       
####################################
# Rules mode
####################################

def rulesMousePressed(event, data):
    if (event.x > data.margin and event.x < data.margin * 3 and event.y > data.margin and event.y < data.margin * 2):
        data.mode = "start"

#switches to game mode
def rulesKeyPressed(event, data):
    pass

def rulesTimerFired(data):
    pass

#Draws block and text
def rulesRedrawAll(canvas, data):
    canvas.create_image(0,0,anchor=NW, image=data.startbg)
    canvas.create_rectangle(data.margin, data.margin, data.margin * 3, data.margin * 2, fill = "blue")
    canvas.create_text(data.margin * 2, data.margin * 1.5, text = "Home", font = "Papyrus 20")
    canvas.create_text(data.width/2, data.height/4 - data.margin * 2,
                       text="Rules", font="Papyrus 50 bold")

                       
####################################
# setup mode
####################################
#if played trump
def foundTrump(data, card):
    if int(card[:-1]) == data.trumpNum:
        return True
    return False

#goest to next player
def nextTurn(data):
    if data.turn[-1] == "4":
        data.turn = "Player1"
    else:
        data.turn = "Player" + str(int(data.turn[-1]) + 1)
    
#distributes cards to players
def distributeCards(data):
    numShouldHave  = data.startingHand
    currentlyHave = len(data.me.cards)
    cardsDrawn = ""
    for i in range(numShouldHave - currentlyHave):
        card = data.me.drawCard(data)
        data.cards.remove(card)
        #print(card)
        cardsDrawn += card + " "
    data.me.cardPositions(data)
    return cardsDrawn[:-1]
        
def setupMousePressed(event, data):
    pass

def setupKeyPressed(event, data):
    msg = ""
    msgDic = ""
    msgDistribute = ""
  
    if event.keysym == "space" and data.me.PID == data.turn:
        
        if data.distribute:
            msgDistribute = "distributeCards " + distributeCards(data) + "\n"
            data.mode = "playGame"
            data.turn = data.dictator
        else:
            #draw card
            card = data.me.drawCard(data)
            data.cards.remove(card)
            msg = "playerDrew " + card + "\n"
            nextTurn(data)
            #found trump card
            if foundTrump(data, card):
                data.dictator = data.me.PID
                data.me.isDictator = True
                msgDic = "dictatorIs " + card + "\n"
                data.trumpSuit = card[-1]
                msg = ""
                msgDistribute = "distributeCards " + distributeCards(data) + "\n"
                data.mode = "dictator"
                data.turn = data.dictator   
                data.startingPlayer = data.dictator    
        
    # send the message to other players!
    if (msgDic != ""):
        print("sending: ", msgDic,)
        data.server.send(msgDic.encode())
    if (msgDistribute != ""):
        print("sending: ", msgDistribute,)
        data.server.send(msgDistribute.encode())
    if (msg != ""):
      print ("sending: ", msg,)
      data.server.send(msg.encode())


#process msgs from other clients/server
def setupTimerFired(data):
    # timerFired receives instructions and executes them
    msgDistribute = ""
    while (serverMsg.qsize() > 0):
        msg = serverMsg.get(False)
        #try:
        print("received: ", msg, "\n")
        msg = msg.split()
        command = msg[0]

        if (command == "myIDis"):
          myPID = msg[1]
          data.me.changePID(myPID)

        elif (command == "newPlayer"):
          newPID = msg[1]
          x = data.width/2
          y = data.height/2
          data.others[newPID] = Player(newPID)
          print(data.others)

        elif (command == "dictatorIs"):
            PID = msg[1]
            card = msg[2]
            data.dictator = PID
            data.startingPlayer = PID
            data.others[PID].isDictator = True
            data.trumpSuit = card[-1]
            data.cards.remove(card)        
 
        elif (command == "playerDrew"):
            PID = msg[1]
            card = msg[2]
            data.cards.remove(card)
            nextTurn(data)
            
        elif (command == "distributeCards"):
            PID = msg[1]
            removeCards = msg[2:]
            #remove cards that were drawn
            for card in removeCards:
                data.cards.remove(card)
            nextTurn(data)
            #need to distribute cards
            if len(data.me.cards) < data.startingHand:
                data.distribute = True

            '''except:
                print("failed")'''
        serverMsg.task_done()

#Draws block and text
def setupRedrawAll(canvas, data):
    canvas.create_image(0,0,anchor=NW, image=data.sleekbg)
    
    #instructions
    canvas.create_rectangle(data.width/2 - 2 * data.margin, data.height/2 - 5 * data.margin, data.width/2 + 2 * data.margin, data.height/2 - 4 * data.margin, fill = "green")
    if data.distribute:
        txt = "Draw Rest of Hand!"
    else:
        txt = "Draw Card"
    canvas.create_text(data.width/2, data.height/2 - 4.6 * data.margin, text = txt, fill = "white", font = "Papyrus 20")
    canvas.create_text(data.width/2, data.height/2 - 4.2 * data.margin, text = "Press Space", fill = "white", font = "Papyrus 12")
    
    #draw others
    pos = -1 * math.pi
    for player in data.others:
        if data.turn == player:
            col = "red"
        else:
            col = "white"
        canvas.create_text(data.width/2 +5.5 * data.margin * math.cos(pos), data.height/2 + 5.5 * data.margin * math.sin(pos), text = player, fill = col, font = "Papyrus")
        pos += math.pi/2
    
    #draw cards
    x,y = data.width/2 - 6 * data.margin, data.height - 5 * data.margin
    for card in data.me.cards:
        if x >= data.width/2 + 5 * data.margin:
            x = data.width/2 - 6 * data.margin
            y = data.height - 3 * data.margin
        canvas.create_image(x, y, image = data.cardsImg[card])
        x += data.margin
    
    #Draw waiting for box
    if data.me.PID != data.turn:
        canvas.create_rectangle(data.width/2 - 2 * data.margin, data.height/2 - 5 * data.margin, data.width/2 + 2 * data.margin, data.height/2 - 3 * data.margin, fill = "gray")
        canvas.create_text(data.width/2, data.height/2 - 4 * data.margin, text = "Waiting for " + data.turn, font = "Papyrus 20")
        
    #My Label
    canvas.create_rectangle(10, data.height - data.margin - 10, 10 + 2 * data.margin, data.height - 10, fill = "blue")
    canvas.create_text(10 + data.margin, data.height - data.margin/2 - 10, fill = "white", text = data.me.PID, font = "Papyrus 20")
  
####################################
# Dictator mode
####################################

#swaps two cards from pot and hand
def swap(data, cardDeck, cardHand):
    if data.clickedPot and data.clickedHand:
        print(cardDeck, cardHand)
        data.cards.remove(cardDeck)
        data.cards.append(cardHand)
        data.me.cards.remove(cardHand)
        data.me.cards.append(cardDeck)
        data.clickedPot = False
        data.clickedHand = False
    
#chooses ally
def findAllies(data, x, y):
    allies = ["14c", "14d", "14h", "14s"]
    x_1, y_1 = data.width/2 - 4.5 * data.margin - 40 + data.margin/2, data.height/2 - 2 * data.margin - data.cardHeight/2
    for card in allies:
        if x >= x_1 and x <= x_1 + data.margin and y >= y_1 and y <= y_1 + data.cardHeight:
            return (1, card)
        x_1 += 10 + data.margin
        
    x_2, y_2 = data.width/2 - 0.5 * data.margin + data.margin/2, data.height/2 - 2 * data.margin - data.cardHeight/2
    for card in allies:
        if x >= x_2 and x <= x_2 + data.margin and y >= y_2 and y <= y_2 + data.cardHeight:
            return (2, card)
        x_2 += 10 + data.margin
    return None

#if clicked on pot
def clickedPot(data, x, y):
    x_r, y_r = data.width/2 - 4.5 * data.margin + data.margin/2, data.height/2 - data.cardHeight/2
    for card in data.cards:
        if x >= x_r and x <= x_r + data.margin and y >= y_r and y <= y_r + data.cardHeight:
            return card
        x_r += data.margin  
    return None

#if clicked on personal hand
def clickedPersonalPot(data, ex, ey):
    x,y = data.width/2 - 6.5 * data.margin + data.margin/2, data.height - 4 * data.margin - data.cardHeight/2
    for card in data.me.cards:
        if x >= data.width/2 + 5.5 * data.margin:
            x = data.width/2 - 6.5 * data.margin + data.margin/2
            y = data.height - 2 * data.margin - data.cardHeight/2
        if ex >= x and ex <= x + data.margin and ey >= y and ey <= data.cardHeight + y:
            return card
        x += data.margin
    return None
    
def dictMousePressed(event, data):
    msg = ""
    print(event.x, event.y)
    #if has clicked a button
    ally = findAllies(data, event.x, event.y)
    potPos = clickedPot(data, event.x, event.y)
    handPos = clickedPersonalPot(data, event.x, event.y)
    
    #clicked ally
    if ally != None:
        data.allyCardAppear = ally[0]
        data.allyCard = ally[1]
        msg = "allyCard " + str(data.allyCardAppear) +" " + data.allyCard + "\n"
    
    #click something in pot
    elif potPos != None:
        data.clickedPot = True
        data.potCard = potPos
        
    #click something in Hand
    elif handPos != None:
        data.clickedHand = True
        data.handCard = handPos
        
    #click swap button
    elif event.x >= data.width/2 - 2 * data.margin and event.y >= data.height/2 + 1 * data.margin and event.x <= data.width/2 + 2 * data.margin and event.y <= data.height/2 + 2 * data.margin:
        swap(data, data.potCard, data.handCard)
        msg = "swapCard " + data.potCard + " " + data.handCard + "\n"
    
    #swaps and sends msg of new pot
    elif event.x >= data.width - 10 - data.margin and event.x <= data.width - 10 and event.y >= data.height - 10 - data.margin and event.y <= data.height - 10:
        data.mode = "playGame"
        
    # send the message to other players!
    if (msg != ""):
      print ("sending: ", msg,)
      data.server.send(msg.encode())

#Restarts game when user clicks s
def dictKeyPressed(event, data):
    if (event.keysym == "s"):
        data.mode = "playGame"

def dictTimerFired(data):
    # timerFired receives instructions and executes them
    msgDistribute = ""
    while (serverMsg.qsize() > 0):
        msg = serverMsg.get(False)
        #try:
        print("received: ", msg, "\n")
        msg = msg.split()
        command = msg[0]
        
        #other players drawing cards
        if (command == "distributeCards"):
            PID = msg[1]
            removeCards = msg[2:]
            print("here", removeCards)
            for card in removeCards:
                print(card)
                data.cards.remove(card)
            '''except:
                print("failed")'''
            
        serverMsg.task_done()


#draws text
def dictRedrawAll(canvas, data):
    canvas.create_image(0,0,anchor=NW, image=data.sleekbg)
    canvas.create_text(data.width/2, 2 * data.margin,
                       text="Dictator Mode", fill = "white", font="Papyrus 30 bold")
                       
    #Choose Allies
    canvas.create_text(data.width/2, 3 * data.margin,
                       text="Choose Allies", fill = "white", font="Papyrus 20")
    
    #draw ally choices
    allies = ["14c", "14d", "14h", "14s"]
    x_1, y_1 = data.width/2 - 4 * data.margin - 40 + data.margin/2, data.height/2 - 2 * data.margin
    for card in allies:
        canvas.create_text(x_1, y_1 - 40, text = "First", fill = "white", font = "Papyrus")
        canvas.create_image(x_1, y_1, image = data.cardsImg[card])
        x_1 += 10 + data.margin
    
    x_2, y_2 = data.width/2 + data.margin/2, data.height/2 - 2 * data.margin
    for card in allies:
        canvas.create_text(x_2, y_2 - 40, text = "Second", fill = "white", font = "Papyrus")
        canvas.create_image(x_2, y_2, image = data.cardsImg[card])
        x_2 += 10 + data.margin
        
    #draw pot
    if len(data.cards) == 8:
        x_r, y_r = data.width/2 - 4 * data.margin + data.margin/2, data.height/2 
        for card in data.cards:
            canvas.create_image(x_r, y_r, image = data.cardsImg[card])
            x_r += data.margin
    else:
        canvas.create_rectangle(data.width/2 - 2.5 * data.margin, data.height/2 - data.margin/2, data.width/2 + 2.5 * data.margin, data.height/2 + data.margin/2, fill = "gray")
        canvas.create_text(data.width/2, data.height/2, text = "Waiting for other players", fill = "white", font = "Papyrus 20")
        
    #Swap Button
    canvas.create_rectangle(data.width/2 - 2 * data.margin, data.height/2 + 1 * data.margin, data.width/2 + 2 * data.margin, data.height/2 + 2 * data.margin, fill = "green")
    canvas.create_text(data.width/2, data.height/2 + 1.4 * data.margin, text = "SWAP", fill = "white", font = "Papyrus 15")
    canvas.create_text(data.width/2, data.height/2 + 1.75 * data.margin, text = "Click Card from Pot and Hand", fill = "white", font = "Papyrus 12")
    
    #draw personal cards
    x,y = data.width/2 - 6 * data.margin + data.margin/2, data.height - 4 * data.margin
    for card in data.me.cards:
        if x >= data.width/2 + 6 * data.margin + data.margin/2:
            x = data.width/2 - 6 * data.margin + data.margin/2
            y = data.height - 2 * data.margin
        canvas.create_image(x, y, image = data.cardsImg[card])
        x += data.margin
        
    #Finish Button
    canvas.create_rectangle(data.width - data.margin - 10, data.height - data.margin - 10, data.width - 10, data.height - 10, fill = "blue")
    canvas.create_text(data.width - 10 - data.margin /2, data.height - 10 - data.margin /2, fill = "white", text = "Finish", font = "Papyrus")
    

    
####################################
# playGame mode
####################################

#given array of hands from the round, determine who wins
def whoWon(data):
    winningHand = data.roundCards[0]
    winningSuit = data.roundCards[0][-1] #first suit
    winningRank = int(data.roundCards[0][:-1]) #first rank
    winningIndex = 0
    print("roundCards", data.roundCards)
    for i in range(1, len(data.roundCards)):
        currRank = int(data.roundCards[i][:-1])
        currSuit = data.roundCards[i][-1]
        print("current stuff", currRank, currSuit)
        #following Suit
        if currSuit == winningSuit and currRank > winningRank and winningRank != data.trumpNum:
            winningRank = currRank
            winningIndex = i
        #trump Suit has been played (first)
        elif currSuit == data.trumpSuit and winningSuit != data.trumpSuit and winningRank != data.trumpNum:
            winningRank = currRank
            winningSuit = currSuit
            winningIndex = i
        #trump num has been played
        elif currRank == data.trumpNum and winningRank != data.trumpNum:
            winningRank = currRank
            winningSuit = currSuit
            winningIndex = i
        #trump num and suit have been played
        elif currRank == data.trumpNum and currSuit == data.trumpSuit and winningSuit != data.trumpSuit and winningRank != data.trumpNum:
            winningRank = currRank
            winningSuit = currSuit
            winningIndex = i
        print(winningIndex)
    data.numPlayed = 0
    return winningPlayer(data, winningIndex)

#determines who won
def winningPlayer(data, i):
    print(data.turn[:-1])
    startingPlayer = int(data.turn[-1])
    winningPlayer = startingPlayer + i
    if winningPlayer > 4:
        winningPlayer -= 4
    return "Player" + str(winningPlayer)

#clicked on card
def isOnCard(data, ex, ey):
    print(ex,ey)
    x,y = data.width/2 - 6.5 * data.margin + data.margin/2, data.height - 5 * data.margin - data.cardHeight/2 
    for card in data.me.cards:
        #first row
        if x >= data.width/2 + 5.5 * data.margin + data.margin/2:
            print("here")
            x = data.width/2 - 6.5 * data.margin + data.margin/2
            y = data.height - 3 * data.margin - data.cardHeight/2 
        #second row
        if ex >= x and ex <= x + data.margin and ey >= y and ey <= data.cardHeight + y:
            print(card)
            return card
        x += data.margin
    return None

    
#player is able to play
def isValid(data, card):
    if data.numPlayed != 0:
        
        startHand = data.roundCards[0]
        startNum = int(startHand[:-1])
        startSuit = startHand[-1] #first suit
        #changes suit to trump
        if startNum == data.trumpNum:
            print("changed suit - start")
            startSuit = data.trumpSuit
        #changes card suit to trump
        if card[:-1] == str(data.trumpNum):
            print("changed suit - card")
            cardSuit = data.trumpSuit
        else:
            cardSuit = card[-1]
        
        #following suit, start suit is not trump suit
        if startSuit != data.trumpSuit and cardSuit == startSuit and card[:-1] != str(data.trumpNum):
            print("start not trump")
            return True
                
        
        #following suit, starting suit is trump suit
        elif startSuit == data.trumpSuit and (cardSuit == data.trumpSuit or card[:-1] == str(data.trumpNum)):
            print("start not trump")
            return True
        
        #add case where does not have suit
        else:
            print("does not have")
            #did not start with trump suit
            if startSuit != data.trumpSuit and startNum != data.trumpNum:
                for c in data.me.cards:
                    if startSuit in c and c[:-1] != str(data.trumpNum):
                        return False
            else: #did start with trump suit
                for c in data.me.cards:
                    if startSuit in c or c[:-1] == str(data.trumpNum):
                        return False
    print("last")
    return True
    

#checks if ally card is played
def playedAlly(data, card):
    if card == data.allyCard:
        data.allyCardAppear -= 1
        return True
    return False
    
#checks if done game
def doneGame(data):
    total = 0
    #sum
    for player in data.others:
        total += data.others[player].points
    
    #opposition win
    if total >= 80 and data.ally != "":
        data.mode = "end"
        return "Opposition"
    
    #dictator win
    if total < 80 and len(data.me.cards) == 0:
        data.mode = "end"
        return "Dictator"
    
    else:
        return None
        
    
#determines what happens if user clicks mouse
def playGameMousePressed(event, data):
    msg = ""
    msgWin = ""
    msgAlly = ""
    msgDone = ""
    #if clicked on card
    card = isOnCard(data, event.x, event.y)
    if data.turn == data.me.PID and card != None and isValid(data, card):
        data.me.playCard(card)
        #if played an ally card
        if playedAlly(data, card):
            print("played ally")
            if data.allyCardAppear == 0:
                print("ally")
                data.ally = data.me.PID
                data.me.isAlly = True
                data.me.points = 0
            msgAlly = "allyIs " + card + "\n"
        #adds card to round cards and sends to players
        data.roundCards.append(card)
        msg = "playedCard " + card + "\n"
        data.numPlayed += 1
        nextTurn(data)
        #end of round
        if data.numPlayed == 4:
            data.turn = whoWon(data)
            data.startingPlayer = data.turn
            #adding points
            if data.turn != data.dictator and data.turn != data.ally:
                if data.turn == data.me.PID:
                    data.me.addPoints(data)
                else:
                    data.others[data.turn].addPoints(data)
            #resets
            data.roundCards = []
            data.numPlayed = 0
            msgWin = "someoneWon " + data.turn + "\n"
            #checks if done game
            if doneGame(data) != None:
                data.whoWon = doneGame(data)
                msgDone = "doneGame " + doneGame(data) + "\n"
        
    # send the message to other players!
    if (msg != ""):
        print ("sending: ", msg,)
        data.server.send(msg.encode())
    if (msgWin != ""):
        print ("sending: ", msgWin,)
        data.server.send(msgWin.encode())
    if (msgAlly != ""):
        print ("sending: ", msgAlly,)
        data.server.send(msgAlly.encode()) 
    if (msgDone != ""):
        print ("sending: ", msgDone,)
        data.server.send(msgDone.encode()) 

#determines if user clicks arrow keys
def playGameKeyPressed(event, data):
    msg = ""
        
    # send the message to other players!
    if (msg != ""):
      print ("sending: ", msg,)
      data.server.send(msg.encode())   
    
#what happens every time delay
def playGameTimerFired(data):
    # timerFired receives instructions and executes them
    while (serverMsg.qsize() > 0):
      msg = serverMsg.get(False)
      try:
        print("received: ", msg, "\n")
        msg = msg.split()
        command = msg[0]
        
        #if player played card
        if (command == "playedCard"):
          playerPID = msg[1]
          card = msg[2]
          data.numPlayed += 1
          data.roundCards.append(card) 
          nextTurn(data)
            
        #if someone wins, resets round
        elif (command == "someoneWon"):
            data.turn = msg[2]
            data.startingPlayer = msg[2]
            #add points functionality
            if data.turn != data.dictator and data.turn != data.ally:
                if data.turn == data.me.PID:
                    data.me.addPoints(data)
                else:
                    data.others[data.turn].addPoints(data)
            data.numPlayed = 0
            data.roundCards = []
            
        elif (command == "distributeCards"):
            PID = msg[1]
            removeCards = msg[2:]
            print("here", removeCards)
            for card in removeCards:
                data.cards.remove(card)
        
        #from dictator
        elif (command == "swapCard"):
            data.cards.remove(msg[2])
            data.cards.append(msg[3])
        
        elif (command == "allyCard"):
            data.allyCardAppear = int(msg[2])
            data.allyCard = msg[3]
            
        elif (command == "allyIs"):
            data.allyCardAppear -= 1
            if data.allyCardAppear == 0:
                data.ally = msg[1]
                data.others[msg[1]].points = 0
                data.others[msg[1]].isAlly = True
        
        #finished game
        elif (command == "doneGame"):
            data.whoWon = msg[2]
            data.mode = "end"
            
      except:
        print("failed")
      serverMsg.task_done()    
    pass


#Draws blocks, board, and text
def playGameRedrawAll(canvas, data):
    canvas.create_image(0,0,anchor=NW, image=data.sleekbg)
    
    #info box
    canvas.create_rectangle(data.width - data.margin * 4 - 10, 10, data.width - 10, data.margin * 3 + 10, fill = "green")
    canvas.create_text(data.width - data.margin * 2, 1.5 * data.margin, text = "Dictator: " + data.dictator + "\nAlly: " + data.ally + "\nAlly Card: " + data.allyCard + "\nTrump Number " + str(data.trumpNum) + "\nTrump Suit " + data.trumpSuit, font = "Papyrus")
    
    #draw others
    pos = -1 * math.pi
    for player in data.others:
        if data.turn == player:
            col = "red"
        else:
            col = "white"
        if data.dictator == player:
            colBox = rgbString(255, 204, 0)
            txtBox = "Dictator"
        elif data.ally == player:
            colBox = "orange"
            txtBox = "Ally"
        else:
            colBox = "blue"
            txtBox = data.others[player].points
        #Player Name
        canvas.create_text(data.width/2 + 5.5 * data.margin * math.cos(pos),data.height/2 - data.margin + 5.5 * data.margin * math.sin(pos), text = player, fill = col, font = "Papyrus")
        #Points Box
        canvas.create_rectangle(data.width/2 + 5.5 * data.margin * math.cos(pos) - data.margin/2,  data.height/2 + 6 * data.margin * math.sin(pos) - data.margin/4, data.width/2 + 5.5 * data.margin * math.cos(pos) + data.margin/2, data.height/2 + 6 * data.margin * math.sin(pos) + data.margin/4, fill = colBox, width = 0)
        canvas.create_text(data.width/2 + 5.5 * data.margin * math.cos(pos),  data.height/2 + 6 * data.margin * math.sin(pos), text = txtBox, fill = "white", font = "Papyrus")
        
        pos += math.pi/2
    
    #draw Round Cards
    x_r, y_r = data.width/2 - 2 * data.margin - 20, data.height/2 - data.margin
    for i in range(len(data.roundCards)):
        canvas.create_image(x_r, y_r, image = data.cardsImg[data.roundCards[i]])
        playerI = ""
        if i + int(data.startingPlayer[-1]) > 4:
            playerI = i + int(data.startingPlayer[-1]) - 4
        else:
            playerI = i + int(data.startingPlayer[-1])
        canvas.create_text(x_r, y_r - data.margin, text = playerI, fill = "white", font = "Papyrus")
        x_r += 10 + data.margin
    
    
    #draw cards
    x,y = data.width/2 - 6 * data.margin + data.margin/2, data.height - 5 * data.margin
    for card in data.me.cards:
        #print(x,y)
        if x >= data.width/2 + 6 * data.margin + data.margin/2:
            x = data.width/2 - 6 * data.margin + data.margin/2
            y = data.height - 3 * data.margin
        canvas.create_image(x, y, image = data.cardsImg[card])
        x += data.margin
    
    #waiting for turn
    if data.me.PID != data.turn:
        canvas.create_rectangle(data.width/2 - 2 * data.margin, data.height/2 - 5 * data.margin, data.width/2 + 2 * data.margin, data.height/2 - 3 * data.margin, fill = "gray")
        canvas.create_text(data.width/2, data.height/2 - 4 * data.margin, text = "Waiting for " + data.turn, fill = "white", font = "Papyrus 20")
    else:
        canvas.create_rectangle(data.width/2 - 2 * data.margin, data.height/2 - 5 * data.margin, data.width/2 + 2 * data.margin, data.height/2 - 3 * data.margin, fill = "green")
        canvas.create_text(data.width/2, data.height/2 - 4 * data.margin, text = "Play a Card!", fill = "white", font = "Papyrus 20")
    
    #My Score
    if data.me.isDictator:
        col = rgbString(255, 204, 0)
        txt = "Dictator"
    elif data.me.isAlly:
        col = "orange"
        txt = "Ally"
    else:
        col = "blue"
        txt = "Score: " + str(data.me.points)
    canvas.create_rectangle(data.width - 2 * data.margin - 10, data.height - data.margin - 10, data.width - 10, data.height - 10, fill = col)
    canvas.create_text(data.width - data.margin - 10, data.height - data.margin/2 - 10, fill = "white", text = txt, font = "Papyrus 20")
    
    #My Label
    canvas.create_rectangle(10, data.height - data.margin - 10, 10 + 2 * data.margin, data.height - 10, fill = "blue")
    canvas.create_text(10 + data.margin, data.height - data.margin/2 - 10, fill = "white", text = data.me.PID, font = "Papyrus 20")
                       
####################################
# end mode
####################################

def endMousePressed(event, data):
    pass

#Restarts game when user clicks s
def endKeyPressed(event, data):
    if (event.keysym == "s"):
        init(data)
        data.trumpNum += 1

def endTimerFired(data):
    pass

#draws text
def endRedrawAll(canvas, data):
    canvas.create_image(0,0,anchor=NW, image=data.startbg)
    
    #winning text
    canvas.create_rectangle(0, data.height/2 - 3 * data.margin, data.width, data.height/2 + data.margin, fill = "black")
    canvas.create_text(data.width/2, data.height/2 - data.margin, text = data.whoWon + " Wins!", fill = "white", font = "Papyrus 30")
    
    #Restart
    canvas.create_text(data.width/2, data.height + 3 * data.margin, text = "Press s to restart", fill = "white", font = "Papyrus 20")


####################################
# use the run function as-is
####################################

def run(width, height, serverMsg=None, server=None):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.server = server
    data.serverMsg = serverMsg
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds

    # create the root and the canvas
    root = Tk()
    
    init(data)
    
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

#creates queue of msgs
serverMsg = Queue(100)
#makes thread to handle incoming msgs
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

run(1000, 700, serverMsg, server)




















