from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessFeatureStartPage(BaseType):
    """
    The ability to customize start page
    """

    __type__: Literal["businessFeatureStartPage"] = "businessFeatureStartPage"
