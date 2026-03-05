import socketio
from werkzeug import serving
import threading

sio = socketio.Server(async_mode="threading", cors_allowed_origins="*")
app = socketio.WSGIApp(sio)

clients = set()


@sio.event
def connect(sid, environ):
    print("Client connected:", sid)
    clients.add(sid)


@sio.event
def message(sid, data):
    print("Client:", data)


@sio.event
def disconnect(sid):
    print("Client disconnected:", sid)
    clients.discard(sid)


def server_terminal_chat():
    while True:
        msg = input("Server: ")
        sio.emit("server_message", msg)


threading.Thread(target=server_terminal_chat, daemon=True).start()

print("Server running on port 5000")

# serving.run_simple("0.0.0.0", 5000, app)
serving.run_simple("localhost", 5000, app)