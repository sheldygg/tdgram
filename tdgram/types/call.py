from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import CallState


@dataclass(kw_only=True)
class Call(BaseType):
    """
    Describes a call
    """

    __type__: Literal["call"] = "call"

    id: int
    """Call identifier, not persistent"""
    user_id: int
    """User identifier of the other call participant"""
    is_outgoing: bool
    """True, if the call is outgoing"""
    is_video: bool
    """True, if the call is a video call"""
    state: CallState
    """Call state"""
    group_call_id: int
    """Identifier of the group call associated with the call; 0 if the group call isn't created yet. The group call can be received through the method getGroupCall"""
