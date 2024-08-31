from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import GroupCallParticipant


@dataclass(kw_only=True)
class UpdateGroupCallParticipant(BaseType):
    """
    Information about a group call participant was changed. The updates are sent only after the group call is received through getGroupCall and only if the call is joined or being joined
    """

    __type__: Literal["updateGroupCallParticipant"] = "updateGroupCallParticipant"

    group_call_id: int
    """Identifier of group call"""
    participant: GroupCallParticipant
    """New data about a participant"""
