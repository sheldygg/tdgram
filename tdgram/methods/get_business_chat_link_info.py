from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessChatLinkInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetBusinessChatLinkInfo(BaseMethod):
    """
    Returns information about a business chat link
    """

    __type__: Literal["getBusinessChatLinkInfo"] = "getBusinessChatLinkInfo"
    __returning_type__ = BusinessChatLinkInfo

    link_name: str
    """Name of the link"""
