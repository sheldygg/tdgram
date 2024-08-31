from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CanTransferOwnershipResultOk(BaseType):
    """
    The session can be used
    """

    __type__: Literal["canTransferOwnershipResultOk"] = "canTransferOwnershipResultOk"
