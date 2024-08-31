from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BusinessChatLink


@dataclass(kw_only=True)
class BusinessChatLinks(BaseType):
    """
    Contains a list of business chat links created by the user
    """

    __type__: Literal["businessChatLinks"] = "businessChatLinks"

    links: list[BusinessChatLink]
    """List of links"""
