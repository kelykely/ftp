from tkinter import *
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import threading
def start():
    authorizer = DummyAuthorizer()
    authorizer.add_user("ankit", "ftp", "F:\\", perm="elradfmw")
    #authorizer.add_anonymous("F:/", perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer
    def callback():
        server = FTPServer((entry1.get(), int(entry2.get())), handler)
        server.serve_forever()
    t = threading.Thread(target=callback)
    t.start()


root=Tk()
label1= Label(root, text="enter the IP:")
label2= Label(root, text="enter the port:")

entry1= Entry(root)
entry2= Entry(root)

button1= Button(root, text="START", command=start)
button2= Button(root, text="STOP", command=exit)
label1.grid(row=0, column=0)
entry1.grid(row=0,column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
button1.grid(row=3, columnspan=2)
button2.grid(row=4, columnspan=2)
root.mainloop()
