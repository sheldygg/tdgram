from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CanTransferOwnershipResultPasswordTooFresh(BaseType):
    """
    The 2-step verification was enabled recently, user needs to wait
    """

    __type__: Literal["canTransferOwnershipResultPasswordTooFresh"] = (
        "canTransferOwnershipResultPasswordTooFresh"
    )

    retry_after: int
    """Time left before the session can be used to transfer ownership of a chat, in seconds"""
