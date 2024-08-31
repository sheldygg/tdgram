from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class BlockMessageSenderFromReplies(BaseMethod):
    """
    Blocks an original sender of a message in the Replies chat
    """

    __type__: Literal["blockMessageSenderFromReplies"] = "blockMessageSenderFromReplies"
    __returning_type__ = Ok

    message_id: int
    """The identifier of an incoming message in the Replies chat"""
    delete_message: bool
    """Pass true to delete the message"""
    delete_all_messages: bool
    """Pass true to delete all messages from the same sender"""
    report_spam: bool
    """Pass true to report the sender to the Telegram moderators"""
