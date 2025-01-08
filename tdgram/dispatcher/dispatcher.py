import asyncio

from ..client import Client
from ..methods import GetOption


class Dispatcher:
    def __init__(self):
        pass

    async def _receive_updates(self, client: Client, receive_timeout: float = 2.0):
        await client.tdjson_client.send(GetOption(name="version"))  # Ping to start receiving updates
        while True:
            update = await client.tdjson_client.receive(receive_timeout)
            if update is None:
                continue

            yield update

    async def _polling(self, client: Client, receive_timeout: float = 2.0):
        async for update in self._receive_updates(client, receive_timeout):
            print(update)

    async def start_polling(
        self,
        client: Client,
        receive_timeout: float = 2.0,
    ):
        tasks = [asyncio.create_task(self._polling(client, receive_timeout))]

        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        for task in pending:
            task.cancel()
