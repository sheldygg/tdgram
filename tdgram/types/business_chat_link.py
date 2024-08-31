from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class BusinessChatLink(BaseType):
    """
    Contains information about a business chat link
    """

    __type__: Literal["businessChatLink"] = "businessChatLink"

    link: str
    """The HTTPS link"""
    text: FormattedText
    """Message draft text that will be added to the input field"""
    title: str
    """Link title"""
    view_count: int
    """Number of times the link was used"""
