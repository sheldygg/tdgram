from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventHasAggressiveAntiSpamEnabledToggled(BaseType):
    """
    The has_aggressive_anti_spam_enabled setting of a supergroup was toggled
    """

    __type__: Literal["chatEventHasAggressiveAntiSpamEnabledToggled"] = (
        "chatEventHasAggressiveAntiSpamEnabledToggled"
    )

    has_aggressive_anti_spam_enabled: bool
    """New value of has_aggressive_anti_spam_enabled"""
