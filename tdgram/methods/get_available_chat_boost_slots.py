from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatBoostSlots
from .base import BaseMethod


@dataclass(kw_only=True)
class GetAvailableChatBoostSlots(BaseMethod):
    """
    Returns the list of available chat boost slots for the current user
    """

    __type__: Literal["getAvailableChatBoostSlots"] = "getAvailableChatBoostSlots"
    __returning_type__ = ChatBoostSlots
