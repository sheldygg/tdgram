from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmojiStatus, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetUserEmojiStatus(BaseMethod):
    """
    Changes the emoji status of a user; for bots only
    """

    __type__: Literal["setUserEmojiStatus"] = "setUserEmojiStatus"
    __returning_type__ = Ok

    user_id: int
    """Identifier of the user"""
    emoji_status: EmojiStatus | None = None
    """New emoji status; pass null to switch to the default badge"""
