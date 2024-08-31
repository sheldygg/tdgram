from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class BusinessChatLinkInfo(BaseType):
    """
    Contains information about a business chat link
    """

    __type__: Literal["businessChatLinkInfo"] = "businessChatLinkInfo"

    chat_id: int
    """Identifier of the private chat that created the link"""
    text: FormattedText
    """Message draft text that must be added to the input field"""
