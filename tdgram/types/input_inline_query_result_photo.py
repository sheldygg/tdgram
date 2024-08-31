from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputMessageContent, ReplyMarkup


@dataclass(kw_only=True)
class InputInlineQueryResultPhoto(BaseType):
    """
    Represents link to a JPEG image
    """

    __type__: Literal["inputInlineQueryResultPhoto"] = "inputInlineQueryResultPhoto"

    id: str
    """Unique identifier of the query result"""
    title: str
    """Title of the result, if known"""
    description: str
    """A short description of the result, if known"""
    thumbnail_url: str
    """URL of the photo thumbnail, if it exists"""
    photo_url: str
    """The URL of the JPEG photo (photo size must not exceed 5MB)"""
    photo_width: int
    """Width of the photo"""
    photo_height: int
    """Height of the photo"""
    reply_markup: ReplyMarkup | None = None
    """The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null"""
    input_message_content: InputMessageContent
    """The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessagePhoto, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact"""
