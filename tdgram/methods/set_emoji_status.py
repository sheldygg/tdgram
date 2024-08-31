from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmojiStatus, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetEmojiStatus(BaseMethod):
    """
    Changes the emoji status of the current user; for Telegram Premium users only
    """

    __type__: Literal["setEmojiStatus"] = "setEmojiStatus"
    __returning_type__ = Ok

    emoji_status: EmojiStatus | None = None
    """New emoji status; pass null to switch to the default badge"""
