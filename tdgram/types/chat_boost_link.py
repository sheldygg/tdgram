from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatBoostLink(BaseType):
    """
    Contains an HTTPS link to boost a chat
    """

    __type__: Literal["chatBoostLink"] = "chatBoostLink"

    link: str
    """The link"""
    is_public: bool
    """True, if the link will work for non-members of the chat"""
