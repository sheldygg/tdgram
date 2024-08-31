from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionViewChecksHint(BaseType):
    """
    Suggests the user to view a hint about the meaning of one and two check marks on sent messages
    """

    __type__: Literal["suggestedActionViewChecksHint"] = "suggestedActionViewChecksHint"
