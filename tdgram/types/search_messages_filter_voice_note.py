from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterVoiceNote(BaseType):
    """
    Returns only voice note messages
    """

    __type__: Literal["searchMessagesFilterVoiceNote"] = "searchMessagesFilterVoiceNote"
