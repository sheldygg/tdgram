from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Location


@dataclass(kw_only=True)
class ChatLocation(BaseType):
    """
    Represents a location to which a chat is connected
    """

    __type__: Literal["chatLocation"] = "chatLocation"

    location: Location
    """The location"""
    address: str
    """Location address; 1-64 characters, as defined by the chat owner"""
