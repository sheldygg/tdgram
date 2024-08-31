from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmojiStatuses
from .base import BaseMethod


@dataclass(kw_only=True)
class GetDefaultEmojiStatuses(BaseMethod):
    """
    Returns default emoji statuses for self status
    """

    __type__: Literal["getDefaultEmojiStatuses"] = "getDefaultEmojiStatuses"
    __returning_type__ = EmojiStatuses
