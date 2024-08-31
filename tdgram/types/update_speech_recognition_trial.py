from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateSpeechRecognitionTrial(BaseType):
    """
    The parameters of speech recognition without Telegram Premium subscription has changed
    """

    __type__: Literal["updateSpeechRecognitionTrial"] = "updateSpeechRecognitionTrial"

    max_media_duration: int
    """The maximum allowed duration of media for speech recognition without Telegram Premium subscription, in seconds"""
    weekly_count: int
    """The total number of allowed speech recognitions per week; 0 if none"""
    left_count: int
    """Number of left speech recognition attempts this week"""
    next_reset_date: int
    """Point in time (Unix timestamp) when the weekly number of tries will reset; 0 if unknown"""
