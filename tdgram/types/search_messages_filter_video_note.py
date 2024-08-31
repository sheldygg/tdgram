from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterVideoNote(BaseType):
    """
    Returns only video note messages
    """

    __type__: Literal["searchMessagesFilterVideoNote"] = "searchMessagesFilterVideoNote"
