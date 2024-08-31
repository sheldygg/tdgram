from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class GroupCallStream(BaseType):
    """
    Describes an available stream in a group call
    """

    __type__: Literal["groupCallStream"] = "groupCallStream"

    channel_id: int
    """Identifier of an audio/video channel"""
    scale: int
    """Scale of segment durations in the stream. The duration is 1000/(2**scale) milliseconds"""
    time_offset: int
    """Point in time when the stream currently ends; Unix timestamp in milliseconds"""
