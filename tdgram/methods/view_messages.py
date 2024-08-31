from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSource, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ViewMessages(BaseMethod):
    """
    Informs TDLib that messages are being viewed by the user. Sponsored messages must be marked as viewed only when the entire text of the message is shown on the screen (excluding the button).
    """

    __type__: Literal["viewMessages"] = "viewMessages"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    message_ids: list[int]
    """The identifiers of the messages being viewed"""
    source: MessageSource | None = None
    """Source of the message view; pass null to guess the source based on chat open state"""
    force_read: bool
    """Pass true to mark as read the specified messages even the chat is closed"""
