from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Audio


@dataclass(kw_only=True)
class InlineQueryResultAudio(BaseType):
    """
    Represents an audio file
    """

    __type__: Literal["inlineQueryResultAudio"] = "inlineQueryResultAudio"

    id: str
    """Unique identifier of the query result"""
    audio: Audio
    """Audio file"""
