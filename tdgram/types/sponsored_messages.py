from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import SponsoredMessage


@dataclass(kw_only=True)
class SponsoredMessages(BaseType):
    """
    Contains a list of sponsored messages
    """

    __type__: Literal["sponsoredMessages"] = "sponsoredMessages"

    messages: list[SponsoredMessage]
    """List of sponsored messages"""
    messages_between: int
    """The minimum number of messages between shown sponsored messages, or 0 if only one sponsored message must be shown after all ordinary messages"""
