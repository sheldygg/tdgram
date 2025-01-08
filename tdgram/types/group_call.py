from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import GroupCallRecentSpeaker


@dataclass(kw_only=True)
class GroupCall(BaseType):
    """
    Describes a group call
    """

    __type__: Literal["groupCall"] = "groupCall"

    id: int
    """Group call identifier"""
    title: str
    """Group call title"""
    scheduled_start_date: int
    """Point in time (Unix timestamp) when the group call is expected to be started by an administrator; 0 if it is already active or was ended"""
    enabled_start_notification: bool
    """True, if the group call is scheduled and the current user will receive a notification when the group call starts"""
    is_active: bool
    """True, if the call is active"""
    is_rtmp_stream: bool
    """True, if the chat is an RTMP stream instead of an ordinary video chat"""
    is_joined: bool
    """True, if the call is joined"""
    need_rejoin: bool
    """True, if user was kicked from the call because of network loss and the call needs to be rejoined"""
    can_be_managed: bool
    """True, if the current user can manage the group call"""
    participant_count: int
    """Number of participants in the group call"""
    has_hidden_listeners: bool
    """True, if group call participants, which are muted, aren't returned in participant list"""
    loaded_all_participants: bool
    """True, if all group call participants are loaded"""
    recent_speakers: list[GroupCallRecentSpeaker]
    """At most 3 recently speaking users in the group call"""
    is_my_video_enabled: bool
    """True, if the current user's video is enabled"""
    is_my_video_paused: bool
    """True, if the current user's video is paused"""
    can_enable_video: bool
    """True, if the current user can broadcast video or share screen"""
    mute_new_participants: bool
    """True, if only group call administrators can unmute new participants"""
    can_toggle_mute_new_participants: bool
    """True, if the current user can enable or disable mute_new_participants setting"""
    record_duration: int
    """Duration of the ongoing group call recording, in seconds; 0 if none. An updateGroupCall update is not triggered when value of this field changes, but the same recording goes on"""
    is_video_recorded: bool
    """True, if a video file is being recorded for the call"""
    duration: int
    """Call duration, in seconds; for ended calls only"""
