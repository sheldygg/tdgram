from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputMessageContent, ReplyMarkup


@dataclass(kw_only=True)
class InputInlineQueryResultArticle(BaseType):
    """
    Represents a link to an article or web page
    """

    __type__: Literal["inputInlineQueryResultArticle"] = "inputInlineQueryResultArticle"

    id: str
    """Unique identifier of the query result"""
    url: str
    """URL of the result, if it exists"""
    hide_url: bool
    """True, if the URL must be not shown"""
    title: str
    """Title of the result"""
    description: str
    """A short description of the result"""
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
