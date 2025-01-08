from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarAmount(BaseType):
    """
    Describes a possibly non-integer amount of Telegram Stars
    """

    __type__: Literal["starAmount"] = "starAmount"

    star_count: int
    """The integer amount of Telegram Stars rounded to 0"""
    nanostar_count: int
    """The number of 1/1000000000 shares of Telegram Stars; from -999999999 to 999999999"""
