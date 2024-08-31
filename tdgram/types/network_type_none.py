from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NetworkTypeNone(BaseType):
    """
    The network is not available
    """

    __type__: Literal["networkTypeNone"] = "networkTypeNone"
