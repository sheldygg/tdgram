from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatBoostSlot


@dataclass(kw_only=True)
class ChatBoostSlots(BaseType):
    """
    Contains a list of chat boost slots
    """

    __type__: Literal["chatBoostSlots"] = "chatBoostSlots"

    slots: list[ChatBoostSlot]
    """List of boost slots"""
