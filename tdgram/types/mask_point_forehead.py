from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MaskPointForehead(BaseType):
    """
    The mask is placed relatively to the forehead
    """

    __type__: Literal["maskPointForehead"] = "maskPointForehead"
