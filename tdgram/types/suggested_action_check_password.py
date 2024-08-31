from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionCheckPassword(BaseType):
    """
    Suggests the user to check whether they still remember their 2-step verification password
    """

    __type__: Literal["suggestedActionCheckPassword"] = "suggestedActionCheckPassword"
