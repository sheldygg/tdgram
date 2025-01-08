from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputMessageContent, Ok, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class EditInlineMessageMedia(BaseMethod):
    """
    Edits the media content of a message with a text, an animation, an audio, a document, a photo or a video in an inline message sent via a bot; for bots only
    """

    __type__: Literal["editInlineMessageMedia"] = "editInlineMessageMedia"
    __returning_type__ = Ok

    inline_message_id: str
    """Inline message identifier"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none; for bots only"""
    input_message_content: InputMessageContent
    """New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo"""
