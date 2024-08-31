from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputMessageContent, ReplyMarkup


@dataclass(kw_only=True)
class InputInlineQueryResultDocument(BaseType):
    """
    Represents a link to a file
    """

    __type__: Literal["inputInlineQueryResultDocument"] = "inputInlineQueryResultDocument"

    id: str
    """Unique identifier of the query result"""
    title: str
    """Title of the resulting file"""
    description: str
    """Short description of the result, if known"""
    document_url: str
    """URL of the file"""
    mime_type: str
    """MIME type of the file content; only 'application/pdf' and 'application/zip' are currently allowed"""
    thumbnail_url: str
    """The URL of the file thumbnail, if it exists"""
    thumbnail_width: int
    """Width of the thumbnail"""
    thumbnail_height: int
    """Height of the thumbnail"""
    reply_markup: ReplyMarkup | None = None
    """The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null"""
    input_message_content: InputMessageContent
    """The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageDocument, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact"""
