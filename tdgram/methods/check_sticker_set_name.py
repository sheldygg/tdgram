from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CheckStickerSetNameResult
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckStickerSetName(BaseMethod):
    """
    Checks whether a name can be used for a new sticker set
    """

    __type__: Literal["checkStickerSetName"] = "checkStickerSetName"
    __returning_type__ = CheckStickerSetNameResult

    name: str
    """Name to be checked"""
