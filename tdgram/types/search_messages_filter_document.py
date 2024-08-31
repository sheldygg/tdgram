from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterDocument(BaseType):
    """
    Returns only document messages
    """

    __type__: Literal["searchMessagesFilterDocument"] = "searchMessagesFilterDocument"
