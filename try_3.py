# Import the required module for text 
# to speech conversion
from gtts import gTTS
 
# This module is imported so that we can 
# play the converted audio
import os
with open("b.txt","r") as file:
# The text that you want to convert to audio
	mytext = file.readlines()
 
# Language in which you want to convert
	language = 'en'
 
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
	myobj = gTTS(text=str(mytext), lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named
# welcome 
	myobj.save("Audio_Doc.mp3")
 
# Playing the converted file
	os.system("mpg321 Audio_Doc.mp3")