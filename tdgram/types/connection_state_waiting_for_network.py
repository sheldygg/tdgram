from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ConnectionStateWaitingForNetwork(BaseType):
    """
    Waiting for the network to become available. Use setNetworkType to change the available network type
    """

    __type__: Literal["connectionStateWaitingForNetwork"] = "connectionStateWaitingForNetwork"
