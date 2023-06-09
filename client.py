import websockets
import asyncio

async def client():
    host = 'ws://localhost:1234'

    async with websockets.connect(host) as connection:
        message = input('Enter your message:')
        await connection.send(message)

        # Добавляем обработку ответа сервера для команды exchange
        if message == "exchange":
            response = await connection.recv()
            print(response)

if __name__ == '__main__':
    asyncio.run(client())
