from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageContactRegistered(BaseType):
    """
    A contact has registered with Telegram
    """

    __type__: Literal["messageContactRegistered"] = "messageContactRegistered"
