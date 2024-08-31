from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ShareChatWithBot(BaseMethod):
    """
    Shares a chat after pressing a keyboardButtonTypeRequestChat button with the bot
    """

    __type__: Literal["shareChatWithBot"] = "shareChatWithBot"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat with the bot"""
    message_id: int
    """Identifier of the message with the button"""
    button_id: int
    """Identifier of the button"""
    shared_chat_id: int
    """Identifier of the shared chat"""
    only_check: bool
    """Pass true to check that the chat can be shared by the button instead of actually sharing it. Doesn't check bot_is_member and bot_administrator_rights restrictions."""
