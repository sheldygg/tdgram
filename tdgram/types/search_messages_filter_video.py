from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterVideo(BaseType):
    """
    Returns only video messages
    """

    __type__: Literal["searchMessagesFilterVideo"] = "searchMessagesFilterVideo"
