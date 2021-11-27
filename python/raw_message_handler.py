import json
import websockets
from game_interface import TotemAnswer
from totem_displayer import TotemDisplayer


def parse_totems(raw_totems):
    totem_list = list()
    for raw_totem in raw_totems:
        totem_list.append(TotemAnswer.from_dict(raw_totem))
    return totem_list


class RawMessageHandler:
    uri = "ws://127.0.0.1:8765"

    def __init__(self):
        self.displayer = TotemDisplayer()

    async def run(self, raw_message, unused):
        async with websockets.connect(self.uri):
            try:
                await self.receive_message(raw_message)
            except websockets.ConnectionClosedError:
                pass

    async def receive_message(self, websocket):
        async for rawMessage in websocket:
            message = json.loads(rawMessage)
            message_type = message['type']
            if message_type == 'REGISTER':
                await websocket.send(rawMessage)
            elif message_type == 'GAMESTATE':
                totem_answers = parse_totems(message['actions']['totems'])
                self.displayer.display(totem_answers)
