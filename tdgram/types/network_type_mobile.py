from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class NetworkTypeMobile(BaseType):
    """
    A mobile network
    """

    __type__: Literal["networkTypeMobile"] = "networkTypeMobile"
