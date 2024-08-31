from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessFeatureOpeningHours(BaseType):
    """
    The ability to set opening hours
    """

    __type__: Literal["businessFeatureOpeningHours"] = "businessFeatureOpeningHours"
