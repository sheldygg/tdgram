from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class SharedChat(BaseType):
    """
    Contains information about a chat shared with a bot
    """

    __type__: Literal["sharedChat"] = "sharedChat"

    chat_id: int
    """Chat identifier"""
    title: str
    """Title of the chat; for bots only"""
    username: str
    """Username of the chat; for bots only"""
    photo: Photo | None = None
    """Photo of the chat; for bots only; may be null"""
