from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class JoinChat(BaseMethod):
    """
    Adds the current user as a new member to a chat. Private and secret chats can't be joined using this method. May return an error with a message 'INVITE_REQUEST_SENT' if only a join request was created
    """

    __type__: Literal["joinChat"] = "joinChat"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
