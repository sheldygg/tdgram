from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeBusinessChat(BaseType):
    """
    The link is a link to a business chat. Use getBusinessChatLinkInfo with the provided link name to get information about the link,
    """

    __type__: Literal["internalLinkTypeBusinessChat"] = "internalLinkTypeBusinessChat"

    link_name: str
    """Name of the link"""
