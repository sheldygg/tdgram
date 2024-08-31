from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventHasProtectedContentToggled(BaseType):
    """
    The has_protected_content setting of a channel was toggled
    """

    __type__: Literal["chatEventHasProtectedContentToggled"] = (
        "chatEventHasProtectedContentToggled"
    )

    has_protected_content: bool
    """New value of has_protected_content"""
