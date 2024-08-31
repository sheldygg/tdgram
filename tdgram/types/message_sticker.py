from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class MessageSticker(BaseType):
    """
    A sticker message
    """

    __type__: Literal["messageSticker"] = "messageSticker"

    sticker: Sticker
    """The sticker description"""
    is_premium: bool
    """True, if premium animation of the sticker must be played"""
