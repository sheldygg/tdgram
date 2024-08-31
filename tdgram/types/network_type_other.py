from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NetworkTypeOther(BaseType):
    """
    A different network type (e.g., Ethernet network)
    """

    __type__: Literal["networkTypeOther"] = "networkTypeOther"
