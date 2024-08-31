from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SpeechRecognitionResultPending(BaseType):
    """
    The speech recognition is ongoing
    """

    __type__: Literal["speechRecognitionResultPending"] = "speechRecognitionResultPending"

    partial_text: str
    """Partially recognized text"""
