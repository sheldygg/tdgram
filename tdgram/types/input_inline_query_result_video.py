from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputMessageContent, ReplyMarkup


@dataclass(kw_only=True)
class InputInlineQueryResultVideo(BaseType):
    """
    Represents a link to a page containing an embedded video player or a video file
    """

    __type__: Literal["inputInlineQueryResultVideo"] = "inputInlineQueryResultVideo"

    id: str
    """Unique identifier of the query result"""
    title: str
    """Title of the result"""
    description: str
    """A short description of the result, if known"""
    thumbnail_url: str
    """The URL of the video thumbnail (JPEG), if it exists"""
    video_url: str
    """URL of the embedded video player or video file"""
    mime_type: str
    """MIME type of the content of the video URL, only 'text/html' or 'video/mp4' are currently supported"""
    video_width: int
    """Width of the video"""
    video_height: int
    """Height of the video"""
    video_duration: int
    """Video duration, in seconds"""
    reply_markup: ReplyMarkup | None = None
    """The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null"""
    input_message_content: InputMessageContent
    """The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageVideo, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact"""
