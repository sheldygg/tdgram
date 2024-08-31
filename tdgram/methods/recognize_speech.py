from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RecognizeSpeech(BaseMethod):
    """
    Recognizes speech in a video note or a voice note message
    """

    __type__: Literal["recognizeSpeech"] = "recognizeSpeech"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message. Use messageProperties.can_recognize_speech to check whether the message is suitable"""
