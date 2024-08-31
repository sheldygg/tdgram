from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageExpiredVideoNote(BaseType):
    """
    A self-destructed video note message
    """

    __type__: Literal["messageExpiredVideoNote"] = "messageExpiredVideoNote"
