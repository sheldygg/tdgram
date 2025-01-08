from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeChatAffiliateProgram(BaseType):
    """
    The link is an affiliate program link. Call searchChatAffiliateProgram with the given username and referrer to process the link
    """

    __type__: Literal["internalLinkTypeChatAffiliateProgram"] = (
        "internalLinkTypeChatAffiliateProgram"
    )

    username: str
    """Username to be passed to searchChatAffiliateProgram"""
    referrer: str
    """Referrer to be passed to searchChatAffiliateProgram"""
