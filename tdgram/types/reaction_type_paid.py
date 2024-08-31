from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReactionTypePaid(BaseType):
    """
    The paid reaction in a channel chat
    """

    __type__: Literal["reactionTypePaid"] = "reactionTypePaid"
