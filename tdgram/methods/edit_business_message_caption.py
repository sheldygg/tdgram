from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessMessage, FormattedText, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class EditBusinessMessageCaption(BaseMethod):
    """
    Edits the caption of a message sent on behalf of a business account; for bots only
    """

    __type__: Literal["editBusinessMessageCaption"] = "editBusinessMessageCaption"
    __returning_type__ = BusinessMessage

    business_connection_id: str
    """Unique identifier of business connection on behalf of which the message was sent"""
    chat_id: int
    """The chat the message belongs to"""
    message_id: int
    """Identifier of the message"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none"""
    caption: FormattedText | None = None
    """New message content caption; pass null to remove caption; 0-getOption('message_caption_length_max') characters"""
    show_caption_above_media: bool
    """Pass true to show the caption above the media; otherwise, the caption will be shown below the media. Can be true only for animation, photo, and video messages"""
