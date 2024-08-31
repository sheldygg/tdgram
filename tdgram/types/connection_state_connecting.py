from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ConnectionStateConnecting(BaseType):
    """
    Establishing a connection to the Telegram servers
    """

    __type__: Literal["connectionStateConnecting"] = "connectionStateConnecting"
