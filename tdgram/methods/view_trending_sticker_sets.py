from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ViewTrendingStickerSets(BaseMethod):
    """
    Informs the server that some trending sticker sets have been viewed by the user
    """

    __type__: Literal["viewTrendingStickerSets"] = "viewTrendingStickerSets"
    __returning_type__ = Ok

    sticker_set_ids: list[int]
    """Identifiers of viewed trending sticker sets"""
