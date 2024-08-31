from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import QuickReplyMessage


@dataclass(kw_only=True)
class QuickReplyMessages(BaseType):
    """
    Contains a list of quick reply messages
    """

    __type__: Literal["quickReplyMessages"] = "quickReplyMessages"

    messages: list[QuickReplyMessage]
    """List of quick reply messages; messages may be null"""
