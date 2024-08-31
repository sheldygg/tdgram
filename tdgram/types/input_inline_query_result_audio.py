from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputMessageContent, ReplyMarkup


@dataclass(kw_only=True)
class InputInlineQueryResultAudio(BaseType):
    """
    Represents a link to an MP3 audio file
    """

    __type__: Literal["inputInlineQueryResultAudio"] = "inputInlineQueryResultAudio"

    id: str
    """Unique identifier of the query result"""
    title: str
    """Title of the audio file"""
    performer: str
    """Performer of the audio file"""
    audio_url: str
    """The URL of the audio file"""
    audio_duration: int
    """Audio file duration, in seconds"""
    reply_markup: ReplyMarkup | None = None
    """The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null"""
    input_message_content: InputMessageContent
    """The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageAudio, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact"""
