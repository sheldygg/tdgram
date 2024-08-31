from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class MessageEffectTypePremiumSticker(BaseType):
    """
    An effect from a premium sticker
    """

    __type__: Literal["messageEffectTypePremiumSticker"] = "messageEffectTypePremiumSticker"

    sticker: Sticker
    """The premium sticker. The effect can be found at sticker.full_type.premium_animation"""
