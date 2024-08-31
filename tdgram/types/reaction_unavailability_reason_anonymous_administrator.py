from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReactionUnavailabilityReasonAnonymousAdministrator(BaseType):
    """
    The user is an anonymous administrator in the supergroup, but isn't a creator of it, so they can't vote on behalf of the supergroup
    """

    __type__: Literal["reactionUnavailabilityReasonAnonymousAdministrator"] = (
        "reactionUnavailabilityReasonAnonymousAdministrator"
    )
