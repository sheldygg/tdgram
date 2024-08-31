from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TargetChat


@dataclass(kw_only=True)
class InternalLinkTypeAttachmentMenuBot(BaseType):
    """
    The link is a link to an attachment menu bot to be opened in the specified or a chosen chat. Process given target_chat to open the chat.
    """

    __type__: Literal["internalLinkTypeAttachmentMenuBot"] = "internalLinkTypeAttachmentMenuBot"

    target_chat: TargetChat
    """Target chat to be opened"""
    bot_username: str
    """Username of the bot"""
    url: str
    """URL to be passed to openWebApp"""
