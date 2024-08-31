from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class GroupCallRecentSpeaker(BaseType):
    """
    Describes a recently speaking participant in a group call
    """

    __type__: Literal["groupCallRecentSpeaker"] = "groupCallRecentSpeaker"

    participant_id: MessageSender
    """Group call participant identifier"""
    is_speaking: bool
    """True, is the user has spoken recently"""
