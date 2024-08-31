from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageLink(BaseType):
    """
    Contains an HTTPS link to a message in a supergroup or channel, or a forum topic
    """

    __type__: Literal["messageLink"] = "messageLink"

    link: str
    """The link"""
    is_public: bool
    """True, if the link will work for non-members of the chat"""
