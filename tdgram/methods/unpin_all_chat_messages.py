from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class UnpinAllChatMessages(BaseMethod):
    """
    Removes all pinned messages from a chat; requires can_pin_messages member right if the chat is a basic group or supergroup, or can_edit_messages administrator right if the chat is a channel
    """

    __type__: Literal["unpinAllChatMessages"] = "unpinAllChatMessages"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat"""
