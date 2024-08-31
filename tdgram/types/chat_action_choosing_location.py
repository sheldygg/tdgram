from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionChoosingLocation(BaseType):
    """
    The user is picking a location or venue to send
    """

    __type__: Literal["chatActionChoosingLocation"] = "chatActionChoosingLocation"
