#!/usr/bin/python3

#CHAT SETTINGS#

fontSizeID = 12         #Font size of the usernames in the chat.
fontTypeID = "Times New Roman"         
fontSizeMessage = 12    #Font size of the messaging in the chat.
fontTypeMessage = "Times New Roman"
fontSizeTimestamp = 12  #Font size of the timestamps in the chat.
fontTypeTimestamp = "Times New Roman"

refreshTime = 1         #Time to wait before seeking new chat messages. 
                        #1=1 second. Accepts decimal increments.

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