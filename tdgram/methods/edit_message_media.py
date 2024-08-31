from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputMessageContent, Message, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class EditMessageMedia(BaseMethod):
    """
    Edits the content of a message with an animation, an audio, a document, a photo or a video, including message caption. If only the caption needs to be edited, use editMessageCaption instead.
    """

    __type__: Literal["editMessageMedia"] = "editMessageMedia"
    __returning_type__ = Message

    chat_id: int
    """The chat the message belongs to"""
    message_id: int
    """Identifier of the message. Use messageProperties.can_be_edited to check whether the message can be edited"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none; for bots only"""
    input_message_content: InputMessageContent
    """New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo"""
