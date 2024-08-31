from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Animations
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSavedAnimations(BaseMethod):
    """
    Returns saved animations
    """

    __type__: Literal["getSavedAnimations"] = "getSavedAnimations"
    __returning_type__ = Animations
