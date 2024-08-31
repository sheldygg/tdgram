from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatStatisticsObjectType


@dataclass(kw_only=True)
class ChatStatisticsInteractionInfo(BaseType):
    """
    Contains statistics about interactions with a message sent in the chat or a story sent by the chat
    """

    __type__: Literal["chatStatisticsInteractionInfo"] = "chatStatisticsInteractionInfo"

    object_type: ChatStatisticsObjectType
    """Type of the object"""
    view_count: int
    """Number of times the object was viewed"""
    forward_count: int
    """Number of times the object was forwarded"""
    reaction_count: int
    """Number of times reactions were added to the object"""
