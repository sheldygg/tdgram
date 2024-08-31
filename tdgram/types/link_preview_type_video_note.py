from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import VideoNote


@dataclass(kw_only=True)
class LinkPreviewTypeVideoNote(BaseType):
    """
    The link is a link to a video note message
    """

    __type__: Literal["linkPreviewTypeVideoNote"] = "linkPreviewTypeVideoNote"

    video_note: VideoNote
    """The video note"""
