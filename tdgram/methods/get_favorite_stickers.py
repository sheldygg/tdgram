from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stickers
from .base import BaseMethod


@dataclass(kw_only=True)
class GetFavoriteStickers(BaseMethod):
    """
    Returns favorite stickers
    """

    __type__: Literal["getFavoriteStickers"] = "getFavoriteStickers"
    __returning_type__ = Stickers
