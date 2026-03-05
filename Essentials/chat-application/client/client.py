import socketio
import threading

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to server")

@sio.event
def server_message(data):
    print("Server:", data)

def client_terminal_chat():
    while True:
        msg = input("Client: ")
        sio.emit("message", msg)

# connect first
sio.connect("http://localhost:5000")

# start thread after connection
threading.Thread(target=client_terminal_chat).start()

sio.wait()