from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CanTransferOwnershipResult
from .base import BaseMethod


@dataclass(kw_only=True)
class CanTransferOwnership(BaseMethod):
    """
    Checks whether the current session can be used to transfer a chat ownership to another user
    """

    __type__: Literal["canTransferOwnership"] = "canTransferOwnership"
    __returning_type__ = CanTransferOwnershipResult
