from time import sleep

from src.joystick.joystick import Joystick
from src.websocket.websocket_server import WebSocketServer

from src.robot.command_parser import CommandParser

def keep_alive():
    sleep(1000000)

if __name__ == '__main__':
    Joystick.start_thread()
    CommandParser.start_joystick_thread()
    
    WebSocketServer.start_thread()
    
    while True:
        keep_alive()