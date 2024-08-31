from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Video


@dataclass(kw_only=True)
class PaidMediaVideo(BaseType):
    """
    The media is a video
    """

    __type__: Literal["paidMediaVideo"] = "paidMediaVideo"

    video: Video
    """The video"""
