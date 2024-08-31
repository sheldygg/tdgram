from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteChatBackground(BaseMethod):
    """
    Deletes background in a specific chat
    """

    __type__: Literal["deleteChatBackground"] = "deleteChatBackground"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    restore_previous: bool
    """Pass true to restore previously set background. Can be used only in private and secret chats with non-deleted users if userFullInfo.set_chat_background == true."""
