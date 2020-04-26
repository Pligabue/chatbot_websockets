#!/usr/bin/env python

# WS server example that synchronizes state across clients

import asyncio
import json
import websockets
from datetime import datetime

async def echo(websocket, content):
    await websocket.send(json.dumps({
        "origin": "bot",
        "content": content + " ECHO",
        "date": datetime.now().isoformat()
    }))

async def counter(websocket, path):
    try:
        async for message in websocket:
            data = json.loads(message)
            await echo(websocket, data["content"])
    except:
        print("Ending connection!")


start_server = websockets.serve(counter, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()