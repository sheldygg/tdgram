from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessFeatureLocation(BaseType):
    """
    The ability to set location
    """

    __type__: Literal["businessFeatureLocation"] = "businessFeatureLocation"
