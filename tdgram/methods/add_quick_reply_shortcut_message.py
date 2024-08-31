from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputMessageContent, QuickReplyMessage
from .base import BaseMethod


@dataclass(kw_only=True)
class AddQuickReplyShortcutMessage(BaseMethod):
    """
    Adds a message to a quick reply shortcut. If shortcut doesn't exist and there are less than getOption('quick_reply_shortcut_count_max') shortcuts, then a new shortcut is created.
    """

    __type__: Literal["addQuickReplyShortcutMessage"] = "addQuickReplyShortcutMessage"
    __returning_type__ = QuickReplyMessage

    shortcut_name: str
    """Name of the target shortcut"""
    reply_to_message_id: int
    """Identifier of a quick reply message in the same shortcut to be replied; pass 0 if none"""
    input_message_content: InputMessageContent
    """The content of the message to be added; inputMessagePoll, inputMessageForwarded and inputMessageLocation with live_period aren't supported"""
