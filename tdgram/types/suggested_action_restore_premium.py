from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionRestorePremium(BaseType):
    """
    Suggests the user to restore a recently expired Premium subscription
    """

    __type__: Literal["suggestedActionRestorePremium"] = "suggestedActionRestorePremium"
