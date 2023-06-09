import websockets
import asyncio

class Server:
    def __init__(self):
        self.clients = set()

    async def test_handler(self, websocket):
        message = await websocket.recv()
        if message == "exchange":
            await self.handle_exchange(websocket)
        else:
            print(message)

    async def handle_exchange(self, websocket):
        # Ваш код для обработки команды exchange
        app = ConsoleApp()
        await app.run()

    async def main(self):
        async with websockets.serve(self.test_handler, 'localhost', 1234):
            await asyncio.Future()

if __name__ == '__main__':
    server = Server()
    asyncio.run(server.main())
