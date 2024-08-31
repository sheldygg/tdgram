from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stickers
from .base import BaseMethod


@dataclass(kw_only=True)
class GetGreetingStickers(BaseMethod):
    """
    Returns greeting stickers from regular sticker sets that can be used for the start page of other users
    """

    __type__: Literal["getGreetingStickers"] = "getGreetingStickers"
    __returning_type__ = Stickers
