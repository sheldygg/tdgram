from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chat
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChat(BaseMethod):
    """
    Returns information about a chat by its identifier; this is an offline request if the current user is not a bot
    """

    __type__: Literal["getChat"] = "getChat"
    __returning_type__ = Chat

    chat_id: int
    """Chat identifier"""
