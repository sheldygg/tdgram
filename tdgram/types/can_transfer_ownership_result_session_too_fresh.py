from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CanTransferOwnershipResultSessionTooFresh(BaseType):
    """
    The session was created recently, user needs to wait
    """

    __type__: Literal["canTransferOwnershipResultSessionTooFresh"] = (
        "canTransferOwnershipResultSessionTooFresh"
    )

    retry_after: int
    """Time left before the session can be used to transfer ownership of a chat, in seconds"""
