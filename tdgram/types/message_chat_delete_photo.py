from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageChatDeletePhoto(BaseType):
    """
    A deleted chat photo
    """

    __type__: Literal["messageChatDeletePhoto"] = "messageChatDeletePhoto"
