from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AffiliateProgramSortOrderRevenue(BaseType):
    """
    The affiliate programs must be sorted by the expected revenue
    """

    __type__: Literal["affiliateProgramSortOrderRevenue"] = "affiliateProgramSortOrderRevenue"
