from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputStoryArea


@dataclass(kw_only=True)
class InputStoryAreas(BaseType):
    """
    Contains a list of story areas to be added
    """

    __type__: Literal["inputStoryAreas"] = "inputStoryAreas"

    areas: list[InputStoryArea]
    """List of input story areas. Currently, a story can have"""
