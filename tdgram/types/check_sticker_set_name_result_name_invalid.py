from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CheckStickerSetNameResultNameInvalid(BaseType):
    """
    The name is invalid
    """

    __type__: Literal["checkStickerSetNameResultNameInvalid"] = (
        "checkStickerSetNameResultNameInvalid"
    )
