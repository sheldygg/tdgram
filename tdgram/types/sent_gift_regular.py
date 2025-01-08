from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Gift


@dataclass(kw_only=True)
class SentGiftRegular(BaseType):
    """
    Regular gift
    """

    __type__: Literal["sentGiftRegular"] = "sentGiftRegular"

    gift: Gift
    """The gift"""
