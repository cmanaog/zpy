
#############################
# ZPY
#############################

import socket
import threading
from queue import Queue

HOST = "" # put your IP address here if playing on multiple computers, everyone else adds that IP addresss and port. sometimes, using localhost will help
PORT = 53231 #change each time you run, all computers use same host and port

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

# events-example0.py from 15-112 website
# Barebones timer, mouse, and keyboard events

import random
import math
from tkinter import *
import copy
from card import *
from image_util import *
#from image_util import *

####################################
# init
####################################

#Initializes Data
def init(data):
    # Game Mode
    data.mode = "start"
    data.margin = 50
    
    data.me = Dot("Lonely", data.width/2, data.height/2)
    data.otherStrangers = dict()
    
    #data.me = Player("Lonely")
    data.others = dict()
    
    #data.image = PhotoImage(file="img/startbg.gif")
    
    #"s" -> Spade, "c" -> Clover, "d" -> Diamond, "h" -> Heart
    data.cards = [(1,"s"), (1, "c"), (1, "d"),(1, "h"),\
    (2,"s"), (2, "c"), (2, "d"),(3, "h"),\
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

#Calls appropriate function for key press based on mode
def keyPressed(event, data):
    #Calls appropriate function for mouse press based on mode
    if (data.mode == "start"): startKeyPressed(event, data)
    elif (data.mode == "playGame"):   playGameKeyPressed(event, data)
    elif (data.mode == "end"):       endKeyPressed(event, data)
    elif (data.mode == "options"):       optionsKeyPressed(event, data)
    elif (data.mode == "rules"):       rulesKeyPressed(event, data)
    elif (data.mode == "setup"):       setupKeyPressed(event, data)
    
#Calls appropriate function for time based on mode
def timerFired(data):
    if (data.mode == "start"): startTimerFired(data)
    elif (data.mode == "playGame"):   playGameTimerFired(data)
    elif (data.mode == "end"):       endTimerFired(data)
    elif (data.mode == "options"):       optionsTimerFired(data)
    elif (data.mode == "rules"):       rulesTimerFired(data)
    elif (data.mode == "setup"):       setupTimerFired(data)
    
#Calls appropriate function for drawing based on mode
def redrawAll(canvas, data):
    if (data.mode == "start"): startRedrawAll(canvas, data)
    elif (data.mode == "playGame"):   playGameRedrawAll(canvas, data)
    elif (data.mode == "end"):       endRedrawAll(canvas, data)
    elif (data.mode == "options"):       optionsRedrawAll(canvas, data)
    elif (data.mode == "rules"):       rulesRedrawAll(canvas, data)
    elif (data.mode == "setup"):       setupRedrawAll(canvas, data)
    
####################################
# start mode
####################################

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
    #canvas.create_image(0,0,anchor=NW, image=data.image)
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
    canvas.create_rectangle(data.margin, data.margin, data.margin * 3, data.margin * 2, fill = "blue")
    canvas.create_text(data.margin * 2, data.margin * 1.5, text = "Home", font = "Papyrus 20")
    canvas.create_text(data.width/2, data.height/4 - data.margin * 2,
                       text="Rules", font="Papyrus 50 bold")

                       
####################################
# setup mode
####################################

def setupMousePressed(event, data):
    pass

#switches to game mode
def setupKeyPressed(event, data):
    dx, dy = 0, 0
    msg = ""

    # moving
    if event.keysym in ["Up", "Down", "Left", "Right"]:
      speed = 5
      if event.keysym == "Up":
        dy = -speed
      elif event.keysym == "Down":
        dy = speed
      elif event.keysym == "Left":
        dx = -speed
      elif event.keysym == "Right":
        dx = speed
      # move myself
      data.me.move(dx, dy)
      # update message to send
      msg = "playerMoved %d %d\n" % (dx, dy)

    # teleporting
    elif event.keysym == "space":
      # get a random coordinate
      x = random.randint(0, data.width)
      y = random.randint(0, data.height)
      # teleport myself
      data.me.teleport(x, y)
      # update the message
      msg = "playerTeleported %d %d\n" % (x, y)
    
    elif event.keysym == "return":
        #draw card
        card = data.me.drawCard(data.cards)
        msg = "playerDrew $d\n" % (card)
        
    # send the message to other players!
    if (msg != ""):
      print ("sending: ", msg,)
      data.server.send(msg.encode())

#process msgs from other clients/server
def setupTimerFired(data):
    # timerFired receives instructions and executes them
    while (serverMsg.qsize() > 0):
      msg = serverMsg.get(False)
      try:
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
          data.otherStrangers[newPID] = Dot(newPID, x, y)

        elif (command == "playerMoved"):
          PID = msg[1]
          dx = int(msg[2])
          dy = int(msg[3])
          data.otherStrangers[PID].move(dx, dy)

        elif (command == "playerTeleported"):
          PID = msg[1]
          x = int(msg[2])
          y = int(msg[3])
          data.otherStrangers[PID].teleport(x, y)
      except:
        print("failed")
      serverMsg.task_done()

#Draws block and text
def setupRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/4,
                       text="Setup", font="Arial 30 bold")
    canvas.create_text(data.width/2, data.height/2,
                       text="Press p to play!", font="Arial 20")
    # draw other players
    for playerName in data.otherStrangers:
      data.otherStrangers[playerName].drawDot(canvas, "blue")
    # draw me
    data.me.drawDot(canvas, "red")
    
    #draw others
    pos = 0
    for player in data.others:
        canvas.create_oval(data.width/2 * math.cos(pos) - data.margin,data.height/2 * math.sin(pos) - data.margin, data.width /2 * math.cos(pos), data.height/2 * math.sin(pos), fill = "yellow")
        pos += 90
                       
####################################
# playGame mode
####################################
    
#determines what happens if user clicks mouse
def playGameMousePressed(event, data):
    pass

#determines if user clicks arrow keys
def playGameKeyPressed(event, data):
    if event.keysym == "p":
        data.mode = "end"
    
#what happens every time delay
def playGameTimerFired(data):
    pass

#Draws blocks, board, and text
def playGameRedrawAll(canvas, data):
    pass
                       
####################################
# end mode
####################################

def endMousePressed(event, data):
    pass

#Restarts game when user clicks s
def endKeyPressed(event, data):
    if (event.keysym == "s"):
        init(data)

def endTimerFired(data):
    pass

#draws text
def endRedrawAll(canvas, data):
    pass


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
    init(data)
    # create the root and the canvas
    root = Tk()
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




















