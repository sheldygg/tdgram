from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessChatLinks
from .base import BaseMethod


@dataclass(kw_only=True)
class GetBusinessChatLinks(BaseMethod):
    """
    Returns business chat links created for the current account
    """

    __type__: Literal["getBusinessChatLinks"] = "getBusinessChatLinks"
    __returning_type__ = BusinessChatLinks
