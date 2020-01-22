#!/usr/bin/python3

#####    TIME     #####
import time
#####   DEV ENV   #####
from env import *
######
from settings import channel , filterWholeMessage
#NET
import socket
#TK
import tkinter as tk ; import tkinter.ttk as ttk
#RANDOMIZATION
import random

sock = socket.socket()
sock.connect((server,port))

#Initialize the program to authenticate itself as a user and then join
# #chatroom.
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN #{channel}\n".encode('utf-8'))



#Originally resp as per tutorial I'm working off of. :P     #Test message, really.
response = sock.recv(2048).decode('utf-8')
#DEBUG  #Initial response is outside the loop so that it can be thrown away.
print(response)


def send(message):
    sent = sock.send(f"PRIVMSG #{channel} :{message}\n".encode('utf-8'))
    #print(sent)


#--------#  #--------#  #--------#  #--------#  #--------#  #--------#  #--------#
root = tk.Tk()

class Interpeter(tk.Text):

    def __init__(self,filterList:list=["abcdefg"]):

            self.filterList:list = filterList
            self.latestusername = None
            self.latestMessage  = None
            #Create a dictionary holding username:color combos.
            self.colorKey:dict  = []

            super().__init__(root)

    def listen(self):

        #Receive a message from Twitch IRC chat.
        message = sock.recv(2048).decode('utf-8')
        #DEBUG
        #print(f"Initial message received was {message}")
        #Check if Twitch has sent us a ping : respond with PONG!
        if message == "PING :tmi.twitch.tv\r\n":
            sock.send("PONG :tmi.twitch.tv".encode('utf-8'))
            #DEBUG
            #print("PONGED TWITCH!!!")
            return False
        elif message == "":
            return False    #Handle occasional blank string.
        return message
    
    def format(self,string:str):
        
        #Separate the received string into a message and an ID, both mangled.
        
        splitUp  = string.split("!",1)    #Split at first occurence of ! only.
        #Then, repair them.
        username = splitUp[0][1:]
        #Split at first occurence of : only.
        message = ( splitUp[1].split(":",1)[1] )

        return [username,message]
        
    
    def filterMessage(self,message:str,fullCensor:bool):
        
        for word in self.filterList:
            if word in message:
                if fullCensor:
                    message = "***"
                    break
                else:
                    message = message.replace(word,"***")
        
        return message
    
    #FOR TESTING, CURRENTLY ONLY RETURNS WHITE
    def randomHexColor(self):
        color = 0xFFFFFF
        return color

    #Call in tk.after()
    def loop(self):

        reception = self.listen()

        #DEBUG
        #print(reception)

        if reception != False:
            username_and_message = self.format(reception)
            username = username_and_message[0]
            message = username_and_message[1]
            message = self.filterMessage(message,filterWholeMessage)

            if username not in self.colorKey:
                #self.colorKey[username] = self.randomHexColor()
                pass
            
            #DEBUG
            print(f"{username} : {message}")


        self.loop()

                

                 



#

DevInterpreter = Interpeter()
DevInterpreter.grid(row=0,column=0)

#DevInterpreter.loop()

root.after(1000,DevInterpreter.loop)
root.title("PyTwitchChat")
root.mainloop()

            


#####   -------   #####
