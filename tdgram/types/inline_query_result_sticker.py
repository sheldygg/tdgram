from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class InlineQueryResultSticker(BaseType):
    """
    Represents a sticker
    """

    __type__: Literal["inlineQueryResultSticker"] = "inlineQueryResultSticker"

    id: str
    """Unique identifier of the query result"""
    sticker: Sticker
    """Sticker"""
