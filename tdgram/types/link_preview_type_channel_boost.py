from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPhoto


@dataclass(kw_only=True)
class LinkPreviewTypeChannelBoost(BaseType):
    """
    The link is a link to boost a channel chat
    """

    __type__: Literal["linkPreviewTypeChannelBoost"] = "linkPreviewTypeChannelBoost"

    photo: ChatPhoto | None = None
    """Photo of the chat; may be null"""
