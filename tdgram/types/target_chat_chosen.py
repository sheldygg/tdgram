from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TargetChatTypes


@dataclass(kw_only=True)
class TargetChatChosen(BaseType):
    """
    The chat needs to be chosen by the user among chats of the specified types
    """

    __type__: Literal["targetChatChosen"] = "targetChatChosen"

    types: TargetChatTypes
    """Allowed types for the chat"""
