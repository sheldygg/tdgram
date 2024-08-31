from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ReactionType


@dataclass(kw_only=True)
class AvailableReaction(BaseType):
    """
    Represents an available reaction
    """

    __type__: Literal["availableReaction"] = "availableReaction"

    type: ReactionType
    """Type of the reaction"""
    needs_premium: bool
    """True, if Telegram Premium is needed to send the reaction"""
