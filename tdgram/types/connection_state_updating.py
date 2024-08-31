from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ConnectionStateUpdating(BaseType):
    """
    Downloading data supposed to be received while the application was offline
    """

    __type__: Literal["connectionStateUpdating"] = "connectionStateUpdating"
