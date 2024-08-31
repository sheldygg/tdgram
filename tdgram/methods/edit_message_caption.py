from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FormattedText, Message, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class EditMessageCaption(BaseMethod):
    """
    Edits the message content caption. Returns the edited message after the edit is completed on the server side
    """

    __type__: Literal["editMessageCaption"] = "editMessageCaption"
    __returning_type__ = Message

    chat_id: int
    """The chat the message belongs to"""
    message_id: int
    """Identifier of the message. Use messageProperties.can_be_edited to check whether the message can be edited"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none; for bots only"""
    caption: FormattedText | None = None
    """New message content caption; 0-getOption('message_caption_length_max') characters; pass null to remove caption"""
    show_caption_above_media: bool
    """Pass true to show the caption above the media; otherwise, the caption will be shown below the media. Can be true only for animation, photo, and video messages"""
