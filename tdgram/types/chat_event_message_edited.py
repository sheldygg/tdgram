from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class ChatEventMessageEdited(BaseType):
    """
    A message was edited
    """

    __type__: Literal["chatEventMessageEdited"] = "chatEventMessageEdited"

    old_message: Message
    """The original message before the edit"""
    new_message: Message
    """The message after it was edited"""
