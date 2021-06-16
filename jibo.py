# WS client example

import asyncio
import websockets
import base64

filename = "jibo_image.jpg"


async def recieve():
    print('Receive started')
    uri = "ws://10.0.0.226:5001"
    async with websockets.connect(uri) as websocket:
        await websocket.send("You know my diamonds be shining pull up 488 just like what?")
        image = await websocket.recv()
        print(f"Base64 length: {len(image)}")
        image_data = base64.b64decode(image)
        with open(filename, 'wb') as file:
            file.write(image_data)


class Receiver:
    def __init__(self):
        self.photo = ""

    async def get_photo(self):
        await asyncio.get_event_loop().run_until_complete(await recieve())
        return filename
