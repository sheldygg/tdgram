import asyncio

from uuid import uuid4
from ctypes import CDLL, c_int, c_char_p, c_double
from typing import Callable

from .base import BaseTDJsonClient, _JsonLoads, _JsonDumps, json_loads_default, json_dumps_default, base_retort
from ..methods import BaseMethod, Request
from .. import types


def class_name(name: str) -> str:
    return name[0].upper() + name[1:]


class TDJsonClient(BaseTDJsonClient):
    def __init__(
        self,
        lib_path: str,
        json_loads: _JsonLoads = json_loads_default,
        json_dumps: _JsonDumps = json_dumps_default,
    ):
        self.json_dumps = json_dumps
        self.json_loads = json_loads

        self._tdjson = CDLL(lib_path)

        self._td_create_client_id: Callable[[], int] = self._tdjson.td_create_client_id
        self._td_create_client_id.restype = c_int
        self._td_create_client_id.argtypes = []

        self._td_receive: Callable[[int, float], bytes] = self._tdjson.td_receive
        self._td_receive.restype = c_char_p
        self._td_receive.argtypes = [c_double]

        self._td_send: Callable[[int, bytes], None] = self._tdjson.td_send
        self._td_send.restype = None
        self._td_send.argtypes = [c_int, c_char_p]

        self._td_execute: Callable[[bytes], bytes] = self._tdjson.td_execute
        self._td_execute.restype = c_char_p
        self._td_execute.argtypes = [c_char_p]

        self.client_id = self._td_create_client_id()

        self._requests: dict[str, Request] = {}

    def make_request(self, method: BaseMethod) -> Request:
        request_id = str(uuid4())

        method_raw = base_retort.dump(method)
        method_raw.setdefault("@extra", {})["request_id"] = request_id

        request = Request(method=method, method_raw=method_raw)
        self._requests[request_id] = request
        return request

    def parse_update(self, message: dict) -> types.BaseType | None:
        if request := self._requests.pop(message.get("@extra", {}).get("request_id"), None):
            if message["@type"] == "error":
                response = base_retort.load(message, types.Error)
            else:
                response = base_retort.load(message, request.method.__returning_type__)
            request.set_response(response)
            return

        # Must use class_name because TDLib returns first letter of class name in lowercase
        # If you have idea how we can fix it, please create issue
        return base_retort.load(message, getattr(types, class_name(message["@type"])))

    async def receive(self, timeout: float = 2.0) -> types.BaseType | None:
        if response := await asyncio.to_thread(self._td_receive, self.client_id, c_double(timeout)):
            return self.parse_update(self.json_loads(response))

    async def send(self, method: BaseMethod) -> Request:
        request = self.make_request(method)
        await asyncio.to_thread(self._td_send, self.client_id, self.json_dumps(request.method_raw))
        return request

    async def execute(self, method: BaseMethod) -> types.BaseType | None:
        if response := await asyncio.to_thread(
            self._td_execute,
            self.json_dumps(method)
        ):
            return self.parse_update(response)

    async def request(self, method: BaseMethod, timeout: float = 10.0) -> types.BaseType | None:
        request = await self.send(method)
        if timeout <= 0:
            return

        await request.wait(timeout=timeout)
        return request.response
