from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MaskPointMouth(BaseType):
    """
    The mask is placed relatively to the mouth
    """

    __type__: Literal["maskPointMouth"] = "maskPointMouth"
