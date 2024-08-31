from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputMessageContent, QuickReplyMessages
from .base import BaseMethod


@dataclass(kw_only=True)
class AddQuickReplyShortcutMessageAlbum(BaseMethod):
    """
    Adds 2-10 messages grouped together into an album to a quick reply shortcut. Currently, only audio, document, photo and video messages can be grouped into an album.
    """

    __type__: Literal["addQuickReplyShortcutMessageAlbum"] = "addQuickReplyShortcutMessageAlbum"
    __returning_type__ = QuickReplyMessages

    shortcut_name: str
    """Name of the target shortcut"""
    reply_to_message_id: int
    """Identifier of a quick reply message in the same shortcut to be replied; pass 0 if none"""
    input_message_contents: list[InputMessageContent]
    """Contents of messages to be sent. At most 10 messages can be added to an album. All messages must have the same value of show_caption_above_media"""
