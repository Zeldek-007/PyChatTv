#!/usr/bin/python3

#CHANNEL SETTINGS   #CHANNEL MUST BE LOWERCASE
#channel = "zeldek"
#TEST
channel="lana_lux"
channel = channel.lower()

#CHAT SETTINGS#

fontSizeID = 12         #Font size of the usernames in the chat.
fontTypeID = "Times New Roman"         
fontSizeMessage = 12    #Font size of the messaging in the chat.
fontTypeMessage = "Times New Roman"

REFRESH_TIME = 1000         #Time to wait before seeking new chat messages. 
                        #1000=1 second.

#Add words here to have messages filtered if they contain them.
badWords = ["foo","bar"]
#Set whether the entire message is filtered out, or only the filtered words.
filterWholeMessage = False
#Decide whether to allow URL'S.
filterURL = False


#WINDOW SETTINGS#

windowWidth  = 200  #Window Sizing
windowHeight = 200

windowOffsetX = 0   #Window Positioning
windowOffsetY = 0

windowOpacity = 100 #Percentage %

#--------#