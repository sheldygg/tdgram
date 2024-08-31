from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class GroupCallVideoQualityFull(BaseType):
    """
    The best available video quality
    """

    __type__: Literal["groupCallVideoQualityFull"] = "groupCallVideoQualityFull"
