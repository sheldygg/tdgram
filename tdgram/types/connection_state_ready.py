from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ConnectionStateReady(BaseType):
    """
    There is a working connection to the Telegram servers
    """

    __type__: Literal["connectionStateReady"] = "connectionStateReady"
