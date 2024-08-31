from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stickers
from .base import BaseMethod


@dataclass(kw_only=True)
class GetRecentStickers(BaseMethod):
    """
    Returns a list of recently used stickers
    """

    __type__: Literal["getRecentStickers"] = "getRecentStickers"
    __returning_type__ = Stickers

    is_attached: bool
    """Pass true to return stickers and masks that were recently attached to photos or video files; pass false to return recently sent stickers"""
