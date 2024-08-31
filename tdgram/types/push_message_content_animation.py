from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Animation


@dataclass(kw_only=True)
class PushMessageContentAnimation(BaseType):
    """
    An animation message (GIF-style).
    """

    __type__: Literal["pushMessageContentAnimation"] = "pushMessageContentAnimation"

    animation: Animation | None = None
    """Message content; may be null"""
    caption: str
    """Animation caption"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
