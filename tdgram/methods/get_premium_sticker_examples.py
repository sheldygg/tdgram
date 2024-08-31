from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stickers
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPremiumStickerExamples(BaseMethod):
    """
    Returns examples of premium stickers for demonstration purposes
    """

    __type__: Literal["getPremiumStickerExamples"] = "getPremiumStickerExamples"
    __returning_type__ = Stickers
