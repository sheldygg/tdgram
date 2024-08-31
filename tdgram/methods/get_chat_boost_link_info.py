from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatBoostLinkInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatBoostLinkInfo(BaseMethod):
    """
    Returns information about a link to boost a chat. Can be called for any internal link of the type internalLinkTypeChatBoost
    """

    __type__: Literal["getChatBoostLinkInfo"] = "getChatBoostLinkInfo"
    __returning_type__ = ChatBoostLinkInfo

    url: str
    """The link to boost a chat"""
