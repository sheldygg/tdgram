from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RateSpeechRecognition(BaseMethod):
    """
    Rates recognized speech in a video note or a voice note message
    """

    __type__: Literal["rateSpeechRecognition"] = "rateSpeechRecognition"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message"""
    is_good: bool
    """Pass true if the speech recognition is good"""
