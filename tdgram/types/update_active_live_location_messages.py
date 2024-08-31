from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class UpdateActiveLiveLocationMessages(BaseType):
    """
    The list of messages with active live location that need to be updated by the application has changed. The list is persistent across application restarts only if the message database is used
    """

    __type__: Literal["updateActiveLiveLocationMessages"] = "updateActiveLiveLocationMessages"

    messages: list[Message]
    """The list of messages with active live locations"""
