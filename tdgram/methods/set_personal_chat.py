from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetPersonalChat(BaseMethod):
    """
    Changes the personal chat of the current user
    """

    __type__: Literal["setPersonalChat"] = "setPersonalChat"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the new personal chat; pass 0 to remove the chat. Use getSuitablePersonalChats to get suitable chats"""
