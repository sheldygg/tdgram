from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Messages
from .base import BaseMethod


@dataclass(kw_only=True)
class SendQuickReplyShortcutMessages(BaseMethod):
    """
    Sends messages from a quick reply shortcut. Requires Telegram Business subscription
    """

    __type__: Literal["sendQuickReplyShortcutMessages"] = "sendQuickReplyShortcutMessages"
    __returning_type__ = Messages

    chat_id: int
    """Identifier of the chat to which to send messages. The chat must be a private chat with a regular user"""
    shortcut_id: int
    """Unique identifier of the quick reply shortcut"""
    sending_id: int
    """Non-persistent identifier, which will be returned back in messageSendingStatePending object and can be used to match sent messages and corresponding updateNewMessage updates"""
