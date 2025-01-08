from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Audio


@dataclass(kw_only=True)
class LinkPreviewTypeAudio(BaseType):
    """
    The link is a link to an audio
    """

    __type__: Literal["linkPreviewTypeAudio"] = "linkPreviewTypeAudio"

    audio: Audio
    """The audio description"""
