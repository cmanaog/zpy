#############################
# ZPY Server
#############################

import socket
import threading
from queue import Queue

HOST = "" # put your IP address here if playing on multiple computers, everyone else adds that IP addresss and port. sometimes, using localhost will help
PORT = 18231 #change each time you run, all computers use same host and port
BACKLOG = 4 #num clients able to join

#creates server, connects to host and port, and listens for connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((HOST,PORT))
server.listen(BACKLOG)
print("looking for connection")

def handleClient(client, serverChannel, cID, clientele):
  client.setblocking(1)
  msg = ""
  while True:
    try:
      msg += client.recv(10).decode("UTF-8") #receives msg and decodes it
      command = msg.split("\n") #newline to signify msg has ended
      while (len(command) > 1):
        readyMsg = command[0]
        msg = "\n".join(command[1:])
        serverChannel.put(str(cID) + " " + readyMsg) #puts msg on server thread
        command = msg.split("\n")
    except:
      # we failed
      return

def serverThread(clientele, serverChannel):
  while True: #figures out who sent msg
    msg = serverChannel.get(True, None) 
    print("msg recv: ", msg)
    msgList = msg.split(" ")
    senderID = msgList[0]
    instruction = msgList[1]
    details = " ".join(msgList[2:])
    if (details != ""): #format msg
      for cID in clientele:
        if cID != senderID: 
          sendMsg = instruction + " " + senderID + " " + details + "\n"
          clientele[cID].send(sendMsg.encode())
          print("> sent to %s:" % cID, sendMsg[:-1])
    print()
    serverChannel.task_done()

#dictionary of clients and number of players
clientele = dict()
playerNum = 0

serverChannel = Queue(100) #queue of string instructions
threading.Thread(target = serverThread, args = (clientele, serverChannel)).start() #server thread

names = ["Player1", "Player2", "Player3", "Player4"]

while True:
  client, address = server.accept() #let other clients join
  # myID is the key to the client in the clientele dictionary
  myID = names[playerNum]
  print(myID, playerNum)
  for cID in clientele:
    print (repr(cID), repr(playerNum))
    clientele[cID].send(("newPlayer %s\n" % myID).encode()) #let everyone else know new player has come
    client.send(("newPlayer %s\n" % cID).encode()) #lets other players add new player to client list
  clientele[myID] = client #new client is added to list
  client.send(("myIDis %s \n" % myID).encode())
  print("connection recieved from %s" % myID)
  #new thread started for client
  threading.Thread(target = handleClient, args = 
                        (client ,serverChannel, myID, clientele)).start()
  playerNum += 1

# Above Code from 15-112 website on Sockets