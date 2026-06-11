import asyncio
import websockets


async def client():
    uri = 'ws://localhost:8765'
    async with websockets.connect(uri) as websocket:
        msg = f'Привет, сервер!'
        print(f'Отправка сообщения серверу: {msg}')
        await websocket.send(msg)

        for el in range(5):
            response = await websocket.recv()
            print(f'{response}')


asyncio.run(client())
