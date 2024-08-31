from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class VideoChat(BaseType):
    """
    Describes a video chat
    """

    __type__: Literal["videoChat"] = "videoChat"

    group_call_id: int
    """Group call identifier of an active video chat; 0 if none. Full information about the video chat can be received through the method getGroupCall"""
    has_participants: bool
    """True, if the video chat has participants"""
    default_participant_id: MessageSender | None = None
    """Default group call participant identifier to join the video chat; may be null"""
