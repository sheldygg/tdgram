from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPhoto


@dataclass(kw_only=True)
class LinkPreviewTypeSupergroupBoost(BaseType):
    """
    The link is a link to boost a supergroup chat
    """

    __type__: Literal["linkPreviewTypeSupergroupBoost"] = "linkPreviewTypeSupergroupBoost"

    photo: ChatPhoto | None = None
    """Photo of the chat; may be null"""
