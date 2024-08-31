from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatBackground


@dataclass(kw_only=True)
class ChatEventBackgroundChanged(BaseType):
    """
    The chat background was changed
    """

    __type__: Literal["chatEventBackgroundChanged"] = "chatEventBackgroundChanged"

    old_background: ChatBackground | None = None
    """Previous background; may be null if none"""
    new_background: ChatBackground | None = None
    """New background; may be null if none"""
