from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class StartGroupCallRecording(BaseMethod):
    """
    Starts recording of an active group call. Requires groupCall.can_be_managed group call flag
    """

    __type__: Literal["startGroupCallRecording"] = "startGroupCallRecording"
    __returning_type__ = Ok

    group_call_id: int
    """Group call identifier"""
    title: str
    """Group call recording title; 0-64 characters"""
    record_video: bool
    """Pass true to record a video file instead of an audio file"""
    use_portrait_orientation: bool
    """Pass true to use portrait orientation for video instead of landscape one"""
