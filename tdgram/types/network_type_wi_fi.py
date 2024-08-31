from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NetworkTypeWiFi(BaseType):
    """
    A Wi-Fi network
    """

    __type__: Literal["networkTypeWiFi"] = "networkTypeWiFi"
