from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventLogFilters(BaseType):
    """
    Represents a set of filters used to obtain a chat event log
    """

    __type__: Literal["chatEventLogFilters"] = "chatEventLogFilters"

    message_edits: bool
    """True, if message edits need to be returned"""
    message_deletions: bool
    """True, if message deletions need to be returned"""
    message_pins: bool
    """True, if pin/unpin events need to be returned"""
    member_joins: bool
    """True, if members joining events need to be returned"""
    member_leaves: bool
    """True, if members leaving events need to be returned"""
    member_invites: bool
    """True, if invited member events need to be returned"""
    member_promotions: bool
    """True, if member promotion/demotion events need to be returned"""
    member_restrictions: bool
    """True, if member restricted/unrestricted/banned/unbanned events need to be returned"""
    info_changes: bool
    """True, if changes in chat information need to be returned"""
    setting_changes: bool
    """True, if changes in chat settings need to be returned"""
    invite_link_changes: bool
    """True, if changes to invite links need to be returned"""
    video_chat_changes: bool
    """True, if video chat actions need to be returned"""
    forum_changes: bool
    """True, if forum-related actions need to be returned"""
