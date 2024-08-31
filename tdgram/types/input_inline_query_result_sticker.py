from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputMessageContent, ReplyMarkup


@dataclass(kw_only=True)
class InputInlineQueryResultSticker(BaseType):
    """
    Represents a link to a WEBP, TGS, or WEBM sticker
    """

    __type__: Literal["inputInlineQueryResultSticker"] = "inputInlineQueryResultSticker"

    id: str
    """Unique identifier of the query result"""
    thumbnail_url: str
    """URL of the sticker thumbnail, if it exists"""
    sticker_url: str
    """The URL of the WEBP, TGS, or WEBM sticker (sticker file size must not exceed 5MB)"""
    sticker_width: int
    """Width of the sticker"""
    sticker_height: int
    """Height of the sticker"""
    reply_markup: ReplyMarkup | None = None
    """The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null"""
    input_message_content: InputMessageContent
    """The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageSticker, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact"""
