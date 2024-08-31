from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ClearRecentStickers(BaseMethod):
    """
    Clears the list of recently used stickers
    """

    __type__: Literal["clearRecentStickers"] = "clearRecentStickers"
    __returning_type__ = Ok

    is_attached: bool
    """Pass true to clear the list of stickers recently attached to photo or video files; pass false to clear the list of recently sent stickers"""
