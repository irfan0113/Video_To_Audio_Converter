import tkinter as tk
import moviepy.editor as audcon
from tkinter import *
from tkinter import messagebox,filedialog

def CreatWidgets():
    sourceLabel = Label(root, text="Video Path: ", bg="#971B1B", font=('Comic Sans', 10,'bold'))
    sourceLabel.grid(row=1, column=1, padx=5, pady=20)

    root.sourceEntry = Entry(root, width=35, textvariable=source)
    root.sourceEntry.grid(row=1, column=2, padx=5, pady=20)

    destinationLabel = Label(root, text="Audio Path: ", bg="#971B1B", font=('Comic Sans', 10,'bold'))
    destinationLabel.grid(row=3, column=1, padx=5, pady=20)

    root.destinationEntry = Entry(root, width=35, textvariable=destination)
    root.destinationEntry.grid(row=3, column=2, padx=5, pady=20)

    SourceButton = Button(root, text="Browse", command=SBrowse, width=10)
    SourceButton.grid(row=1, column=3, padx=5, pady=20)

    DestinationButton = Button(root, text="Browse", command=DBrowse, width=10)
    DestinationButton.grid(row=3, column=3, padx=5, pady=20)

    ConvertButton = Button(root, text="Convert Video", command=Convert, width=30)
    ConvertButton.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

    # name = Label(root, text="Software by Muhammed Irfan", font=('Ariel', 8, 'bold'))
    # name.grid(row=4, column=1, padx=5, pady=20)

def SBrowse():

    videoName = filedialog.askopenfilename(initialdir="C:\Python\PyVideo2Audio", filetypes=(("MP4 (*.mp4)","*.mp4"), ("AVI (*.avi)", "*.avi"),("All File")))
    root.sourceEntry.insert(0, videoName)

def DBrowse():
    audioName = filedialog.asksaveasfilename(initialdir="C:\Python\PyVideo2Audio", defaultextension=".mp3", filetypes=(("MP3 (*.mp3)", "*.mp3"), ("WAV (*.wav)", "*.wav"), ("All File")))
    root.destinationEntry.insert(0,audioName)

def Convert():
    sourceFile = source.get()
    destinationFile = destination.get()

    sourceVideo = audcon.VideoFileClip(sourceFile)
    sourceVideo.audio.write_audiofile(destinationFile)

    messagebox.showinfo("SUCCESS", "Video Converted Successfully")

root = tk.Tk()

root.title("Video To Audio Software By Muhammed Irfan")
root.config(bg="#971B1B")
root.geometry("440x170")
root.resizable(False, False)

source = StringVar()
destination = StringVar()

CreatWidgets()

root.mainloop()
