from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InternalLinkType


@dataclass(kw_only=True)
class TargetChatInternalLink(BaseType):
    """
    The chat needs to be open with the provided internal link
    """

    __type__: Literal["targetChatInternalLink"] = "targetChatInternalLink"

    link: InternalLinkType
    """An internal link pointing to the chat"""
