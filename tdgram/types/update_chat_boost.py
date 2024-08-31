from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatBoost


@dataclass(kw_only=True)
class UpdateChatBoost(BaseType):
    """
    A chat boost has changed; for bots only
    """

    __type__: Literal["updateChatBoost"] = "updateChatBoost"

    chat_id: int
    """Chat identifier"""
    boost: ChatBoost
    """New information about the boost"""
