from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterAudio(BaseType):
    """
    Returns only audio messages
    """

    __type__: Literal["searchMessagesFilterAudio"] = "searchMessagesFilterAudio"
