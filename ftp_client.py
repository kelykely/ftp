from tkinter import *
from ftplib import FTP
import ftplib

ftp = FTP('')


def connect():
    ftp.connect(e1.get(), int(e2.get()))
    ftp.login(user=e8.get(), passwd=e9.get())
    print("connected successfully")


def upload():
    a=e3.get()
    ftp.storbinary('STOR '+a, open(a, 'rb'))
    print("FILE uploaded successfully")


def download():
    a=e3.get()
    ftp.retrbinary('RETR ' + a, open(a, 'wb').write)
    print('File successfully downloaded.')


def show():
    print('Directory of', ftp.pwd())
    ftp.dir()


def close():
    ftp.quit()
    print('Goodbye!')
    exit()


def change():
    ftp.cwd(e4.get())
    print('Directory of', ftp.pwd())
    ftp.dir()
    print('Current Directory', ftp.pwd())


root = Tk()
l1 = Label(root, text="enter the IP:")
l2 = Label(root, text="enter the port:")
e1 = Entry(root)
e2 = Entry(root)
b1 = Button(root, text="CONNECT", command=connect)

l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)
l8 = Label(root, text="enter the username:")
l9 = Label(root, text="enter the password:")
e8 = Entry(root)
e9 = Entry(root)
l8.grid(row=2, column=0)
e8.grid(row=2, column=1)
l9.grid(row=3, column=0)
e9.grid(row=3, column=1)

b1.grid(row=4, columnspan=2)

l3 = Label(root, text="enter the filename:")
e3 = Entry(root)

l3.grid(row=5, column=0)
e3.grid(row=5, column=1)
b2 = Button(root, text="Download", command=download)
b2.grid(row=6, columnspan=2)
b3 = Button(root, text="UPLOAD", command=upload)
b3.grid(row=7, columnspan=2)

l4 = Label(root, text="enter the dir:")
e4 = Entry(root)
b4 = Button(root, text="change directory", command=change)

l4.grid(row=11, column=0)
e4.grid(row=11, column=1)
b4.grid(row=12, columnspan=2)

b5 = Button(root, text="EXIT", bg="black", fg="red", command=close)
b5.grid(row=18, columnspan=2)

b6 = Button(root, text="SHOW FILES", command=show)
b6.grid(row=17,columnspan=2)
root.mainloop()
