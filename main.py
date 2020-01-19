#!/usr/bin/python3

#####   TKINTER   #####
import tkinter as tk ; import tkinter.ttk as ttk
#####    TIME     #####
import time
#####   DEV ENV   #####
from env import *

#NET
import socket
import requests

sock = socket.socket()
sock.connect((server,port))

#This is the one part of the code I don't understand so far. I mean, I get what it's doing ; I just don't understand the syntax of the string it's sending.
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN #{channel}\n".encode('utf-8'))

#Originally resp as per tutorial I'm working off of. :P     #Test message, really.
response = sock.recv(2048).decode('utf-8')
print(response)

#:ixw1234!ixw1234@ixw1234.tmi.twitch.tv PRIVMSG #roninpawn :gotta import copy
'''
def send(self, chan, msg):
    self.irc.send("PRIVMSG " + chan + " :" + msg + "\n")

'''

def connect():
    rooms = requests.get(url=URL)
    print(rooms)

def send(message):
    sent = sock.send(f"PRIVMSG #{channel} :{message}\n".encode('utf-8'))
    print(sent)

#connect()
send("now imagine this code without any comments")

while True:
    response = sock.recv(2048).decode('utf-8')
    print(response)

response = sock.recv(2048).decode('utf-8')
print(response)


######

#from settings import *



#--------#  #--------#  #--------#  #--------#  #--------#  #--------#  #--------#

#Create root window.
root = tk.Tk()

#Create the chatbox.
chat = tk.Text(root)


#Username of the streamer.
streamerID = channel
#Username a chat message belongs to.
chattingID = "SomeRando"
#Content of a message.
messageTxt = "Hello, world!"
#Timestamp of a message.
postedTime = "00:00:00"


#Create a dictionary holding username:color combos.

class Interpeter():

    def interpret(self):

        #Receive a message from Twitch IRC chat.
        message = sock.recv(2048).decode('utf-8')
        #Check if Twitch has sent us a ping.
        if message == "PING :tmi.twitch.tv":
            sock.send("PONG :tmi.twitch.tv".encode('utf-8'))
        #Check if the received message needs filtering.
        elif True:
            pass


    def __init__(self):
        pass

#####   -------   #####


#root.mainloop()
