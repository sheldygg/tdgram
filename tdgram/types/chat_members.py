from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatMember


@dataclass(kw_only=True)
class ChatMembers(BaseType):
    """
    Contains a list of chat members
    """

    __type__: Literal["chatMembers"] = "chatMembers"

    total_count: int
    """Approximate total number of chat members found"""
    members: list[ChatMember]
    """A list of chat members"""
