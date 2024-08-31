from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FactCheck


@dataclass(kw_only=True)
class UpdateMessageFactCheck(BaseType):
    """
    A fact-check added to a message was changed
    """

    __type__: Literal["updateMessageFactCheck"] = "updateMessageFactCheck"

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Message identifier"""
    fact_check: FactCheck
    """The new fact-check"""
