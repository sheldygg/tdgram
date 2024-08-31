from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ClearRecentEmojiStatuses(BaseMethod):
    """
    Clears the list of recently used emoji statuses for self status
    """

    __type__: Literal["clearRecentEmojiStatuses"] = "clearRecentEmojiStatuses"
    __returning_type__ = Ok
