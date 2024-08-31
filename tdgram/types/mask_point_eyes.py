from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MaskPointEyes(BaseType):
    """
    The mask is placed relatively to the eyes
    """

    __type__: Literal["maskPointEyes"] = "maskPointEyes"
