from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Animation


@dataclass(kw_only=True)
class Animations(BaseType):
    """
    Represents a list of animations
    """

    __type__: Literal["animations"] = "animations"

    animations: list[Animation]
    """List of animations"""
