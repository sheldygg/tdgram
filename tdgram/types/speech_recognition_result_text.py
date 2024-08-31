from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SpeechRecognitionResultText(BaseType):
    """
    The speech recognition successfully finished
    """

    __type__: Literal["speechRecognitionResultText"] = "speechRecognitionResultText"

    text: str
    """Recognized text"""
