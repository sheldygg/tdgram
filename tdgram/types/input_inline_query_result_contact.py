from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Contact, InputMessageContent, ReplyMarkup


@dataclass(kw_only=True)
class InputInlineQueryResultContact(BaseType):
    """
    Represents a user contact
    """

    __type__: Literal["inputInlineQueryResultContact"] = "inputInlineQueryResultContact"

    id: str
    """Unique identifier of the query result"""
    contact: Contact
    """User contact"""
    thumbnail_url: str
    """URL of the result thumbnail, if it exists"""
    thumbnail_width: int
    """Thumbnail width, if known"""
    thumbnail_height: int
    """Thumbnail height, if known"""
    reply_markup: ReplyMarkup | None = None
    """The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null"""
    input_message_content: InputMessageContent
    """The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact"""
