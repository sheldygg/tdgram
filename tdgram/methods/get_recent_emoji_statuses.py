from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmojiStatuses
from .base import BaseMethod


@dataclass(kw_only=True)
class GetRecentEmojiStatuses(BaseMethod):
    """
    Returns recent emoji statuses for self status
    """

    __type__: Literal["getRecentEmojiStatuses"] = "getRecentEmojiStatuses"
    __returning_type__ = EmojiStatuses
