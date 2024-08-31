from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputMessageContent, ReplyMarkup


@dataclass(kw_only=True)
class InputInlineQueryResultAnimation(BaseType):
    """
    Represents a link to an animated GIF or an animated (i.e., without sound) H.264/MPEG-4 AVC video
    """

    __type__: Literal["inputInlineQueryResultAnimation"] = "inputInlineQueryResultAnimation"

    id: str
    """Unique identifier of the query result"""
    title: str
    """Title of the query result"""
    thumbnail_url: str
    """URL of the result thumbnail (JPEG, GIF, or MPEG4), if it exists"""
    thumbnail_mime_type: str | None = None
    """MIME type of the video thumbnail. If non-empty, must be one of 'image/jpeg', 'image/gif' and 'video/mp4'"""
    video_url: str
    """The URL of the video file (file size must not exceed 1MB)"""
    video_mime_type: str
    """MIME type of the video file. Must be one of 'image/gif' and 'video/mp4'"""
    video_duration: int
    """Duration of the video, in seconds"""
    video_width: int
    """Width of the video"""
    video_height: int
    """Height of the video"""
    reply_markup: ReplyMarkup | None = None
    """The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null"""
    input_message_content: InputMessageContent
    """The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageAnimation, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact"""
