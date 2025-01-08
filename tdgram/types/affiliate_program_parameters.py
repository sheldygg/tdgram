from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AffiliateProgramParameters(BaseType):
    """
    Describes parameters of an affiliate program
    """

    __type__: Literal["affiliateProgramParameters"] = "affiliateProgramParameters"

    commission_per_mille: int
    """The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the program owner;"""
    month_count: int
    """Number of months the program will be active; 0-36. If 0, then the program is eternal"""
