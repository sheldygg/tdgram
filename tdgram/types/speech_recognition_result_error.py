from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Error


@dataclass(kw_only=True)
class SpeechRecognitionResultError(BaseType):
    """
    The speech recognition failed
    """

    __type__: Literal["speechRecognitionResultError"] = "speechRecognitionResultError"

    error: Error
    """Recognition error. An error with a message 'MSG_VOICE_TOO_LONG' is returned when media duration is too big to be recognized"""
