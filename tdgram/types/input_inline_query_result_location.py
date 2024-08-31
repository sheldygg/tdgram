from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputMessageContent, Location, ReplyMarkup


@dataclass(kw_only=True)
class InputInlineQueryResultLocation(BaseType):
    """
    Represents a point on the map
    """

    __type__: Literal["inputInlineQueryResultLocation"] = "inputInlineQueryResultLocation"

    id: str
    """Unique identifier of the query result"""
    location: Location
    """Location result"""
    live_period: int
    """Amount of time relative to the message sent time until the location can be updated, in seconds"""
    title: str
    """Title of the result"""
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
