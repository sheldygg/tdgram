from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmojiStatuses
from .base import BaseMethod


@dataclass(kw_only=True)
class GetThemedEmojiStatuses(BaseMethod):
    """
    Returns up to 8 emoji statuses, which must be shown right after the default Premium Badge in the emoji status list for self status
    """

    __type__: Literal["getThemedEmojiStatuses"] = "getThemedEmojiStatuses"
    __returning_type__ = EmojiStatuses
