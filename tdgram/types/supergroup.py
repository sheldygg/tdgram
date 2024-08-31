from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatMemberStatus, Usernames


@dataclass(kw_only=True)
class Supergroup(BaseType):
    """
    Represents a supergroup or channel with zero or more members (subscribers in the case of channels). From the point of view of the system, a channel is a special kind of a supergroup:
    """

    __type__: Literal["supergroup"] = "supergroup"

    id: int
    """Supergroup or channel identifier"""
    usernames: Usernames | None = None
    """Usernames of the supergroup or channel; may be null"""
    date: int
    """Point in time (Unix timestamp) when the current user joined, or the point in time when the supergroup or channel was created, in case the user is not a member"""
    status: ChatMemberStatus
    """Status of the current user in the supergroup or channel; custom title will always be empty"""
    member_count: int
    """Number of members in the supergroup or channel; 0 if unknown. Currently, it is guaranteed to be known only if the supergroup or channel was received through"""
    boost_level: int
    """Approximate boost level for the chat"""
    has_linked_chat: bool
    """True, if the channel has a discussion group, or the supergroup is the designated discussion group for a channel"""
    has_location: bool
    """True, if the supergroup is connected to a location, i.e. the supergroup is a location-based supergroup"""
    sign_messages: bool
    """True, if messages sent to the channel contains name of the sender. This field is only applicable to channels"""
    show_message_sender: bool
    """True, if messages sent to the channel have information about the sender user. This field is only applicable to channels"""
    join_to_send_messages: bool
    """True, if users need to join the supergroup before they can send messages. Always true for channels and non-discussion supergroups"""
    join_by_request: bool
    """True, if all users directly joining the supergroup need to be approved by supergroup administrators. Always false for channels and supergroups without username, location, or a linked chat"""
    is_slow_mode_enabled: bool
    """True, if the slow mode is enabled in the supergroup"""
    is_channel: bool
    """True, if the supergroup is a channel"""
    is_broadcast_group: bool
    """True, if the supergroup is a broadcast group, i.e. only administrators can send messages and there is no limit on the number of members"""
    is_forum: bool
    """True, if the supergroup is a forum with topics"""
    is_verified: bool
    """True, if the supergroup or channel is verified"""
    has_sensitive_content: bool
    """True, if content of media messages in the supergroup or channel chat must be hidden with 18+ spoiler"""
    restriction_reason: str | None = None
    """If non-empty, contains a human-readable description of the reason why access to this supergroup or channel must be restricted"""
    is_scam: bool
    """True, if many users reported this supergroup or channel as a scam"""
    is_fake: bool
    """True, if many users reported this supergroup or channel as a fake account"""
    has_active_stories: bool
    """True, if the supergroup or channel has non-expired stories available to the current user"""
    has_unread_active_stories: bool
    """True, if the supergroup or channel has unread non-expired stories available to the current user"""
