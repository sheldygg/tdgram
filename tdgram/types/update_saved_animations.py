from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateSavedAnimations(BaseType):
    """
    The list of saved animations was updated
    """

    __type__: Literal["updateSavedAnimations"] = "updateSavedAnimations"

    animation_ids: list[int]
    """The new list of file identifiers of saved animations"""
