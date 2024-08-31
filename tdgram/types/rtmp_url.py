from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class RtmpUrl(BaseType):
    """
    Represents an RTMP URL
    """

    __type__: Literal["rtmpUrl"] = "rtmpUrl"

    url: str
    """The URL"""
    stream_key: str
    """Stream key"""
