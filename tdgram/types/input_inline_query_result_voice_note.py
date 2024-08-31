from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputMessageContent, ReplyMarkup


@dataclass(kw_only=True)
class InputInlineQueryResultVoiceNote(BaseType):
    """
    Represents a link to an opus-encoded audio file within an OGG container, single channel audio
    """

    __type__: Literal["inputInlineQueryResultVoiceNote"] = "inputInlineQueryResultVoiceNote"

    id: str
    """Unique identifier of the query result"""
    title: str
    """Title of the voice note"""
    voice_note_url: str
    """The URL of the voice note file"""
    voice_note_duration: int
    """Duration of the voice note, in seconds"""
    reply_markup: ReplyMarkup | None = None
    """The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null"""
    input_message_content: InputMessageContent
    """The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageVoiceNote, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact"""
