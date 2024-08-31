from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NetworkTypeMobileRoaming(BaseType):
    """
    A mobile roaming network
    """

    __type__: Literal["networkTypeMobileRoaming"] = "networkTypeMobileRoaming"
