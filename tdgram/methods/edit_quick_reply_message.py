from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputMessageContent, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class EditQuickReplyMessage(BaseMethod):
    """
    Asynchronously edits the text, media or caption of a quick reply message. Use quickReplyMessage.can_be_edited to check whether a message can be edited.
    """

    __type__: Literal["editQuickReplyMessage"] = "editQuickReplyMessage"
    __returning_type__ = Ok

    shortcut_id: int
    """Unique identifier of the quick reply shortcut with the message"""
    message_id: int
    """Identifier of the message"""
    input_message_content: InputMessageContent
    """New content of the message. Must be one of the following types: inputMessageText, inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo"""
