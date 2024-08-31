from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPhoto


@dataclass(kw_only=True)
class MessageChatChangePhoto(BaseType):
    """
    An updated chat photo
    """

    __type__: Literal["messageChatChangePhoto"] = "messageChatChangePhoto"

    photo: ChatPhoto
    """New chat photo"""
