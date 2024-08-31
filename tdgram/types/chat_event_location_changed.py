from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatLocation


@dataclass(kw_only=True)
class ChatEventLocationChanged(BaseType):
    """
    The supergroup location was changed
    """

    __type__: Literal["chatEventLocationChanged"] = "chatEventLocationChanged"

    old_location: ChatLocation | None = None
    """Previous location; may be null"""
    new_location: ChatLocation | None = None
    """New location; may be null"""
