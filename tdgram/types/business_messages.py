from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BusinessMessage


@dataclass(kw_only=True)
class BusinessMessages(BaseType):
    """
    Contains a list of messages from a business account as received by a bot
    """

    __type__: Literal["businessMessages"] = "businessMessages"

    messages: list[BusinessMessage]
    """List of business messages"""
