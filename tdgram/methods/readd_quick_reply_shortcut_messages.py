from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import QuickReplyMessages
from .base import BaseMethod


@dataclass(kw_only=True)
class ReaddQuickReplyShortcutMessages(BaseMethod):
    """
    Readds quick reply messages which failed to add. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed.
    """

    __type__: Literal["readdQuickReplyShortcutMessages"] = "readdQuickReplyShortcutMessages"
    __returning_type__ = QuickReplyMessages

    shortcut_name: str
    """Name of the target shortcut"""
    message_ids: list[int]
    """Identifiers of the quick reply messages to readd. Message identifiers must be in a strictly increasing order"""
