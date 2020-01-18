#!/usr/bin/python3

from env import *

import socket

sock = socket.socket()
sock.connect((server,port))

#This is the one part of the code I don't understand so far. I mean, I get what it's doing ; I just don't understand the syntax of the string it's sending.
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

#Originally resp as per tutorial I'm working off of. :P     #Test message, really.
response = sock.recv(2048).decode('utf-8')
print(response)

#Settings#


fontID = 12         #Font size of the usernames in the chat.
fontMessage = 12    #Font size of the messaging in the chat.
fontTimestamp = 12  #Font size of the timestamps in the chat.


#--------#

#####   TKINTER   #####
import tkinter as tk ; import tkinter.ttk as ttk

root = tk.Tk()
chatView = tk.Label(text=("#BEGIN CHAT LOG FOR STREAMER:"+channel))

#####   -------   #####

#
while True:
    pass