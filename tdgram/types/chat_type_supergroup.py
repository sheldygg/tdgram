from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatTypeSupergroup(BaseType):
    """
    A supergroup or channel (with unlimited members)
    """

    __type__: Literal["chatTypeSupergroup"] = "chatTypeSupergroup"

    supergroup_id: int
    """Supergroup or channel identifier"""
    is_channel: bool
    """True, if the supergroup is a channel"""
