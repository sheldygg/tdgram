from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class UpgradedGiftOriginalDetails(BaseType):
    """
    Describes the original details about the gift
    """

    __type__: Literal["upgradedGiftOriginalDetails"] = "upgradedGiftOriginalDetails"

    sender_user_id: int
    """Identifier of the user that sent the gift; 0 if the gift was private"""
    receiver_user_id: int
    """Identifier of the user that received the gift"""
    text: FormattedText
    """Message added to the gift"""
    date: int
    """Point in time (Unix timestamp) when the gift was sent"""
