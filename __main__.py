
import RPi.GPIO as GPIO

from websocket.websocket_server import WebSocketServer

def keep_alive():
    pass

if __name__ == '__main__':
    WebSocketServer.start_thread()
    
    while True:
        keep_alive()