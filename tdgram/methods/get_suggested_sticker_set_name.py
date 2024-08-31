from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSuggestedStickerSetName(BaseMethod):
    """
    Returns a suggested name for a new sticker set with a given title
    """

    __type__: Literal["getSuggestedStickerSetName"] = "getSuggestedStickerSetName"
    __returning_type__ = Text

    title: str
    """Sticker set title; 1-64 characters"""
