from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CanTransferOwnershipResultPasswordNeeded(BaseType):
    """
    The 2-step verification needs to be enabled first
    """

    __type__: Literal["canTransferOwnershipResultPasswordNeeded"] = (
        "canTransferOwnershipResultPasswordNeeded"
    )
