from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterVoiceAndVideoNote(BaseType):
    """
    Returns only voice and video note messages
    """

    __type__: Literal["searchMessagesFilterVoiceAndVideoNote"] = (
        "searchMessagesFilterVoiceAndVideoNote"
    )
