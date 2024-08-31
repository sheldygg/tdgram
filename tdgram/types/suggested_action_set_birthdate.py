from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionSetBirthdate(BaseType):
    """
    Suggests the user to set birthdate
    """

    __type__: Literal["suggestedActionSetBirthdate"] = "suggestedActionSetBirthdate"
