from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReactionUnavailabilityReasonGuest(BaseType):
    """
    The user isn't a member of the supergroup and can't send messages and reactions there without joining
    """

    __type__: Literal["reactionUnavailabilityReasonGuest"] = "reactionUnavailabilityReasonGuest"
