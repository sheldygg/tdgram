from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionSetProfilePhoto(BaseType):
    """
    Suggests the user to set profile photo
    """

    __type__: Literal["suggestedActionSetProfilePhoto"] = "suggestedActionSetProfilePhoto"
