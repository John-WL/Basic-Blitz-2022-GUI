import asyncio
import websockets
from raw_message_handler import RawMessageHandler


async def run():
    async with websockets.serve(RawMessageHandler().run, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(run())
