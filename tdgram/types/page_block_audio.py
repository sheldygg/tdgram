from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Audio, PageBlockCaption


@dataclass(kw_only=True)
class PageBlockAudio(BaseType):
    """
    An audio file
    """

    __type__: Literal["pageBlockAudio"] = "pageBlockAudio"

    audio: Audio | None = None
    """Audio file; may be null"""
    caption: PageBlockCaption
    """Audio file caption"""
