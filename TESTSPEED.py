"""

TestNet app by Hamed Masoudi

"""
from tkinter import *
import webbrowser
import tkinter.messagebox
import speedtest
print("The TestNet is measuring your speed\nPlease wait...")
s=speedtest.Speedtest()
dr=s.download()/1024/1024
print("Your download speed was measured")
print("Wait a second....")
ur=s.upload()/1024/1024
print("Your upload speed was measured")
pr=s.results.ping
print("Your ping speed was measured\n\n")


print("DONE :) ")

class TestNet:
    def __init__(self):
        self.root=Tk()
        self.root.title("TestNet")
        self.root.geometry('550x300')
        color = 'white'
        self.root.configure(bg=color)
        self.root.resizable(width=True, height=True)
        self.m =Text(height=3, width=300)
        self.m.configure(font=('arial', 13, 'italic'))
        self.m.pack()
        self.m.insert(END,"Welcome to TestNet app, you can see your internet speed by clicking on specific button")
        self.btn_download=Button( text="Download Test", font=('arial', 25, 'italic'), fg="red",
                            command=self.Download)
        self.btn_download.pack(side=TOP)
        self.btn_upload=Button( text="Upload Test", font=('arial', 25, 'italic'), fg="blue",
                        command=self.Upload)
        self.btn_upload.pack(side=TOP)
        self.btn_ping=Button( text="Ping Test", font=('arial', 25, 'italic'), fg="green",
                           command=self.Ping)
        self.btn_ping.pack(side=TOP)

        self.root.mainloop()
        
    def Download(self):
        self.do=Tk()
        self.do.title("TestDownload")
        self.do.geometry('500x300')
        self.T =Text(self.do,height=3, width=300)
        self.T.configure(font=('arial', 13, 'italic'),fg="red")
        self.T.pack()
        self.T.insert(END,f"Your download speed is:{dr:.2f}mbit/s")
    def Upload(self):
        self.Up=Tk()
        self.Up.title("TestUpload")
        self.Up.geometry('500x300')
        # ur=s.upload()
        self.T =Text(self.Up,height=3, width=300)
        self.T.configure(font=('arial', 13, 'italic'),fg="blue")
        self.T.pack()
        self.T.insert(END,f"Your upload speed is:{ur:.2f}mbit/s")
    def Ping(self):
        self.pp=Tk()
        self.pp.title("TestPing")
        self.pp.geometry('500x300')
        # pr=s.results.ping
        self.T =Text(self.pp,height=3, width=300)
        self.T.configure(font=('arial', 13, 'italic'),fg="blue")
        self.T.pack()
        self.T.insert(END,f"Your ping speed is:{pr}ms")
TestNet()