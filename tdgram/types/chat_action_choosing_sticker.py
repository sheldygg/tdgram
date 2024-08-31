from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionChoosingSticker(BaseType):
    """
    The user is picking a sticker to send
    """

    __type__: Literal["chatActionChoosingSticker"] = "chatActionChoosingSticker"
