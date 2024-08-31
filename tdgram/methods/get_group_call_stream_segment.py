from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FilePart, GroupCallVideoQuality
from .base import BaseMethod


@dataclass(kw_only=True)
class GetGroupCallStreamSegment(BaseMethod):
    """
    Returns a file with a segment of a group call stream in a modified OGG format for audio or MPEG-4 format for video
    """

    __type__: Literal["getGroupCallStreamSegment"] = "getGroupCallStreamSegment"
    __returning_type__ = FilePart

    group_call_id: int
    """Group call identifier"""
    time_offset: int
    """Point in time when the stream segment begins; Unix timestamp in milliseconds"""
    scale: int
    """Segment duration scale; 0-1. Segment's duration is 1000/(2**scale) milliseconds"""
    channel_id: int
    """Identifier of an audio/video channel to get as received from tgcalls"""
    video_quality: GroupCallVideoQuality | None = None
    """Video quality as received from tgcalls; pass null to get the worst available quality"""
