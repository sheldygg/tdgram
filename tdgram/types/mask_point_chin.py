from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MaskPointChin(BaseType):
    """
    The mask is placed relatively to the chin
    """

    __type__: Literal["maskPointChin"] = "maskPointChin"
