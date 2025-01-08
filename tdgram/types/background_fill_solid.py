from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BackgroundFillSolid(BaseType):
    """
    Describes a solid fill of a background
    """

    __type__: Literal["backgroundFillSolid"] = "backgroundFillSolid"

    color: int
    """A color of the background in the RGB format"""
