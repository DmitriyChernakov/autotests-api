import asyncio

import websockets


async def users_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"

        await websocket.send(message)

        for _ in range(5):
            response = await websocket.recv()
            print(response)


asyncio.run(users_client())
