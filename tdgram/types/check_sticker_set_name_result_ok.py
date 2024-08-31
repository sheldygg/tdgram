from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CheckStickerSetNameResultOk(BaseType):
    """
    The name can be set
    """

    __type__: Literal["checkStickerSetNameResultOk"] = "checkStickerSetNameResultOk"
