import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

import asyncio

from threading import Thread
from websockets.server import serve

from robot.command_parser import CommandParser

class WebSocketServer:
    @staticmethod
    async def echo(websocket):
        async for message in websocket:
            CommandParser.parse(message)
            await websocket.send('done!')

    @staticmethod
    async def main():
        async with serve(WebSocketServer.echo, "0.0.0.0", 8765):
            await asyncio.Future()

    @staticmethod
    def start():
        asyncio.run(WebSocketServer.main())
        
    @staticmethod
    def start_thread():
        process = Thread(target=WebSocketServer.start, daemon=True)
        process.start()