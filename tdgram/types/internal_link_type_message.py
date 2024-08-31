from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeMessage(BaseType):
    """
    The link is a link to a Telegram message or a forum topic. Call getMessageLinkInfo with the given URL to process the link,
    """

    __type__: Literal["internalLinkTypeMessage"] = "internalLinkTypeMessage"

    url: str
    """URL to be passed to getMessageLinkInfo"""
