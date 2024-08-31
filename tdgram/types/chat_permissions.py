from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatPermissions(BaseType):
    """
    Describes actions that a user is allowed to take in a chat
    """

    __type__: Literal["chatPermissions"] = "chatPermissions"

    can_send_basic_messages: bool
    """True, if the user can send text messages, contacts, giveaways, giveaway winners, invoices, locations, and venues"""
    can_send_audios: bool
    """True, if the user can send music files"""
    can_send_documents: bool
    """True, if the user can send documents"""
    can_send_photos: bool
    """True, if the user can send photos"""
    can_send_videos: bool
    """True, if the user can send videos"""
    can_send_video_notes: bool
    """True, if the user can send video notes"""
    can_send_voice_notes: bool
    """True, if the user can send voice notes"""
    can_send_polls: bool
    """True, if the user can send polls"""
    can_send_other_messages: bool
    """True, if the user can send animations, games, stickers, and dice and use inline bots"""
    can_add_link_previews: bool
    """True, if the user may add a link preview to their messages"""
    can_change_info: bool
    """True, if the user can change the chat title, photo, and other settings"""
    can_invite_users: bool
    """True, if the user can invite new users to the chat"""
    can_pin_messages: bool
    """True, if the user can pin messages"""
    can_create_topics: bool
    """True, if the user can create topics"""
