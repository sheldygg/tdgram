from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionConvertToBroadcastGroup(BaseType):
    """
    Suggests the user to convert specified supergroup to a broadcast group
    """

    __type__: Literal["suggestedActionConvertToBroadcastGroup"] = (
        "suggestedActionConvertToBroadcastGroup"
    )

    supergroup_id: int
    """Supergroup identifier"""
