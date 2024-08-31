from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputMessageContent, InputMessageReplyTo


@dataclass(kw_only=True)
class DraftMessage(BaseType):
    """
    Contains information about a message draft
    """

    __type__: Literal["draftMessage"] = "draftMessage"

    reply_to: InputMessageReplyTo | None = None
    """Information about the message to be replied; must be of the type inputMessageReplyToMessage; may be null if none"""
    date: int
    """Point in time (Unix timestamp) when the draft was created"""
    input_message_text: InputMessageContent
    """Content of the message draft; must be of the type inputMessageText, inputMessageVideoNote, or inputMessageVoiceNote"""
    effect_id: int
    """Identifier of the effect to apply to the message when it is sent; 0 if none"""
