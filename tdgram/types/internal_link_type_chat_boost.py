from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeChatBoost(BaseType):
    """
    The link is a link to boost a Telegram chat. Call getChatBoostLinkInfo with the given URL to process the link.
    """

    __type__: Literal["internalLinkTypeChatBoost"] = "internalLinkTypeChatBoost"

    url: str
    """URL to be passed to getChatBoostLinkInfo"""
