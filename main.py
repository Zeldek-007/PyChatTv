#!/usr/bin/python3

#####    TIME     #####
import time
#####   DEV ENV   #####
from env import *
######
from settings import channel , filterWholeMessage , REFRESH_TIME
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



#Dump the first one or two Twitch messages, which don't need to be shown.
response = sock.recv(2048).decode('utf-8')

'''
UNUSED

def send(message):
    sent = sock.send(f"PRIVMSG #{channel} :{message}\n".encode('utf-8'))
    #print(sent)
'''

#--------#  #--------#  #--------#  #--------#  #--------#  #--------#  #--------#
root = tk.Tk()

class Interpeter(tk.Text):

    def __init__(self,filterList:list=["abcdefg"]):

            #Bad word list.
            self.filterList:list = filterList
            #Create a dictionary holding username:color combos.
            self.colorKey:dict  = {}

            #Init as child Text of root window.
            super().__init__(root,wrap="word")

    def listen(self):

        #Receive a message from Twitch IRC chat.
        message = sock.recv(2048).decode('utf-8')
        #DEBUG
        #print(f"Initial message received was \n {message}")
        #Check if Twitch has sent us a ping : respond with PONG!
        if message == "PING :tmi.twitch.tv\r\n":
            sock.send("PONG :tmi.twitch.tv".encode('utf-8'))
            #DEBUG
            print("PONGED TWITCH!!!")
            return False
        #Get rid of garbage.
        elif message == "" or message == "\n" or message == "\r" or message == "\r\n" or message == " ":
            return False
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
    
    #
    def randomHexColor(self):
        color = random.randint(0x000000,0xFFFFFF)
        color = (str(hex(color)))
        color = "#"+color[2:]
        return color

    #Call in tk.after()
    def loop(self):

        reception = self.listen()
        #If we received a proper message, format and filter it.
        if reception != False:
            username_and_message = self.format(reception)
            username = username_and_message[0]
            message = username_and_message[1]
            message = self.filterMessage(message,filterWholeMessage)

            if username not in self.colorKey:
                self.tag_config(username,foreground=self.randomHexColor())
            
            #ADD USERNAME : MESSAGE to Textbox.
            self.insert(tk.END,f"{username} : {message}\n",username)
            
        #Loop into self.
        root.after(REFRESH_TIME,self.loop)

#DEW IT

DevInterpreter = Interpeter()
DevInterpreter.grid(row=0,column=0)

root.after(REFRESH_TIME,DevInterpreter.loop)
root.title(f"PyTwitchChat: {channel}")
root.mainloop()
