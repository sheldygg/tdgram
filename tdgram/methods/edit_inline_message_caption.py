from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FormattedText, Ok, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class EditInlineMessageCaption(BaseMethod):
    """
    Edits the caption of an inline message sent via a bot; for bots only
    """

    __type__: Literal["editInlineMessageCaption"] = "editInlineMessageCaption"
    __returning_type__ = Ok

    inline_message_id: str
    """Inline message identifier"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none"""
    caption: FormattedText | None = None
    """New message content caption; pass null to remove caption; 0-getOption('message_caption_length_max') characters"""
    show_caption_above_media: bool
    """Pass true to show the caption above the media; otherwise, the caption will be shown below the media. Can be true only for animation, photo, and video messages"""
