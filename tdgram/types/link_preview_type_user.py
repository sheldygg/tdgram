from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatPhoto


@dataclass(kw_only=True)
class LinkPreviewTypeUser(BaseType):
    """
    The link is a link to a user
    """

    __type__: Literal["linkPreviewTypeUser"] = "linkPreviewTypeUser"

    photo: ChatPhoto | None = None
    """Photo of the user; may be null if none"""
    is_bot: bool
    """True, if the user is a bot"""
