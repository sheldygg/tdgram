from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionBarJoinRequest(BaseType):
    """
    The chat is a private chat with an administrator of a chat to which the user sent join request
    """

    __type__: Literal["chatActionBarJoinRequest"] = "chatActionBarJoinRequest"

    title: str
    """Title of the chat to which the join request was sent"""
    is_channel: bool
    """True, if the join request was sent to a channel chat"""
    request_date: int
    """Point in time (Unix timestamp) when the join request was sent"""
