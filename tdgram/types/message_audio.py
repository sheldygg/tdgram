from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Audio, FormattedText


@dataclass(kw_only=True)
class MessageAudio(BaseType):
    """
    An audio message
    """

    __type__: Literal["messageAudio"] = "messageAudio"

    audio: Audio
    """The audio description"""
    caption: FormattedText
    """Audio caption"""
