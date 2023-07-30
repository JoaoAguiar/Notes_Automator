import tkinter

from tkinter import *
from tkinter import messagebox
from pytube import YouTube

def Widgets_GUI():
    root.linkText = Entry(root, width=30, textvariable=link, font="Arial 12")
    root.linkText.place(relx=0.5, rely=0.3, anchor=CENTER)

    downloader_button = Button(root, text="Download", command=Download, width=10, height=1, relief=GROOVE, font="Arial 13", bg="white", fg="black")
    downloader_button.place(relx=0.5, rely=.7, anchor=CENTER)

def Download():
    video_stream = YouTube(link.get(), use_oauth=True, allow_oauth_cache=True).streams.get_highest_resolution()
    video_stream.download()

    messagebox.showinfo("Successfully", "Video Downloaded\n")

root = tkinter.Tk()
root.geometry("300x100")
root.resizable(False, False)
root.title("Youtube Downloader")

link = StringVar()

Widgets_GUI()

root.mainloop()

#https://www.youtube.com/watch?v=GtuPl6-iK7M