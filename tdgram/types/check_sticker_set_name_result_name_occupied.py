from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CheckStickerSetNameResultNameOccupied(BaseType):
    """
    The name is occupied
    """

    __type__: Literal["checkStickerSetNameResultNameOccupied"] = (
        "checkStickerSetNameResultNameOccupied"
    )
