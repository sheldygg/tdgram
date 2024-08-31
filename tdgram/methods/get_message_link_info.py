from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageLinkInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageLinkInfo(BaseMethod):
    """
    Returns information about a public or private message link. Can be called for any internal link of the type internalLinkTypeMessage
    """

    __type__: Literal["getMessageLinkInfo"] = "getMessageLinkInfo"
    __returning_type__ = MessageLinkInfo

    url: str
    """The message link"""
