from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AffiliateProgramSortOrderCreationDate(BaseType):
    """
    The affiliate programs must be sorted by creation date
    """

    __type__: Literal["affiliateProgramSortOrderCreationDate"] = (
        "affiliateProgramSortOrderCreationDate"
    )
