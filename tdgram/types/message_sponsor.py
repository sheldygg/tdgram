from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Photo


@dataclass(kw_only=True)
class MessageSponsor(BaseType):
    """
    Information about the sponsor of a message
    """

    __type__: Literal["messageSponsor"] = "messageSponsor"

    url: str
    """URL of the sponsor to be opened when the message is clicked"""
    photo: Photo | None = None
    """Photo of the sponsor; may be null if must not be shown"""
    info: str
    """Additional optional information about the sponsor to be shown along with the message"""
