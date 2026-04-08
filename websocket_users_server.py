import asyncio

import websockets
from websockets import ServerConnection


async def get_user_message(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        for _, i in enumerate(range(1, 6)):
            response = f"{i} Сообщение пользователя: {message}"
            await websocket.send(response)


async def main():
    server = await websockets.serve(get_user_message, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())
