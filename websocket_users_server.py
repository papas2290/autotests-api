import asyncio
import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    count_msg = 0
    async for message in websocket:

        print(f"Получено сообщение от пользователя: {message}")

        for el in range(5):
            count_msg += 1
            response = f'{count_msg} Сообщение пользователя: {message}'
            await websocket.send(response)



async def main():
    server = await websockets.serve(echo, 'localhost', 8765)
    print('websocket запущен на ws://8765')
    await server.wait_closed()


asyncio.run(main())
