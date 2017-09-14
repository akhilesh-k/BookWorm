#import the 'tkinter' module
import tkinter
import os
import sys
from time import gmtime, strftime
import subprocess

def cnv():		
	
	python3_command = "python try_1.py"  # launch your python2 script using bash

	process = subprocess.Popen(python3_command.split(), stdout=subprocess.PIPE)
	output, error = process.communicate() 
def play():
	os.system("vlc Audio_Doc.mp3")
	sys.exit(0)

def save():
	python3_command = "python try_3.py"  # launch your python2 script using bash

	process = subprocess.Popen(python3_command.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()


#def shwpdf():
#	print("ch4k")
#	python3_command = "python try_2.py"  # launch your python2 script using bash
#
#	process = subprocess.Popen(python3_command.split(), stdout=subprocess.PIPE)
#	output, error = process.communicate()
#	os.system("gedit Summary.txt") 
#def listensum():
#	python3_command = "python trysum.py"  # launch your python2 script using bash
#	process = subprocess.Popen(python3_command.split(), stdout=subprocess.PIPE)
#	output, error = process.communicate()
#	os.system("rhythmbox Summary.mp3")


def main():
	window = tkinter.Tk()
	#set the window background to hex code '#a1dbcd'
	window.configure(background="#1b4f72")
	window.geometry("720x400")
		#set the window title
	window.title("Listenify")
		#set the window icon

	photo = tkinter.PhotoImage(file="aa.png")
	w = tkinter.Label(window, image=photo)
	w.pack()

		#create a label for the instructions
	a1 = tkinter.Label(window, text="Automated Ebook Reader and Summarizer", fg="#383a39", bg="#fff", font=("Helvetica", 22))
	a1.pack()	#and pack it into the window
	

		#create the widgets for entering a username
	b1 = tkinter.Button(window, text="Convert", fg="#383a39", bg="#fff", command=cnv)

		#and pack them into the window
	b1.pack()
	#l2=tkinter.Button(window,text="Read Summary!",relief="raised",command=shwpdf)
	#l2.pack(side="top")
		#create the widgets for entering a username
	d1 = tkinter.Button(window, text="Listen Story", fg="#fff", bg="#383a39", command=play)

		#and pack them into to the window
	d1.pack()
	

		#create a button widget called btn
	btn = tkinter.Button(window, text="Save Story", fg="#383a39", bg="#a1dbcd", command=save)
		#pack the widget into the window
	btn.pack()
	#yy=tkinter.Button(window,text="Listen Summary!",relief="raised",command=listensum)
	#yy.pack(side="top")
	b4 = tkinter.Button(window, text="Quit", fg="#fff", bg="#383a39", command=window.destroy)
		#pack the widget into the window
	b4.pack()
	bottomLabel=tkinter.Label(window, text="Created by ACM Team 4")
	#draw the window, and start the 'application'
	window.mainloop()
main()
