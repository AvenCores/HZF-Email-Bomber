from tkinter import *
from tkinter import messagebox
from os import mkdir
import requests

root = Tk()
root.title('HZF Email Bomber Downloader')
root.geometry('350x120')
root.resizable(width=False, height=False)

def download():
        mkdir("c://Bomber")
        f=open(r'c:/Bomber/HZF Email Bomber.zip',"wb")
        ufr = requests.get("https://github.com/AvenCores/HZF-Email-Bomber/releases/download/V1.0/Email.Bomber.by.HZF.zip")
        f.write(ufr.content)
        f.close()
        messagebox.showinfo(title="Удачно", message='Бомбер был скачен в папку C:\Bomber')
        return "exit"

file = Button(text='Скачать Email Bomber V1.0', command=download)
file.pack()
file.place(x=100, y=30)
poetry = 'Downloader manager by HZF'
label3 = Label(text=poetry, justify=CENTER)
label3.place(x=10, y=90)
root.mainloop()
