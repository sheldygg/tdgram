from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import QuickReplyMessage
from .base import BaseMethod


@dataclass(kw_only=True)
class AddQuickReplyShortcutInlineQueryResultMessage(BaseMethod):
    """
    Adds a message to a quick reply shortcut via inline bot. If shortcut doesn't exist and there are less than getOption('quick_reply_shortcut_count_max') shortcuts, then a new shortcut is created.
    """

    __type__: Literal["addQuickReplyShortcutInlineQueryResultMessage"] = (
        "addQuickReplyShortcutInlineQueryResultMessage"
    )
    __returning_type__ = QuickReplyMessage

    shortcut_name: str
    """Name of the target shortcut"""
    reply_to_message_id: int
    """Identifier of a quick reply message in the same shortcut to be replied; pass 0 if none"""
    query_id: int
    """Identifier of the inline query"""
    result_id: str
    """Identifier of the inline query result"""
    hide_via_bot: bool
    """Pass true to hide the bot, via which the message is sent. Can be used only for bots getOption('animation_search_bot_username'), getOption('photo_search_bot_username'), and getOption('venue_search_bot_username')"""
