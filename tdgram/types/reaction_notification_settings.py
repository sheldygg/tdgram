from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ReactionNotificationSource


@dataclass(kw_only=True)
class ReactionNotificationSettings(BaseType):
    """
    Contains information about notification settings for reactions
    """

    __type__: Literal["reactionNotificationSettings"] = "reactionNotificationSettings"

    message_reaction_source: ReactionNotificationSource
    """Source of message reactions for which notifications are shown"""
    story_reaction_source: ReactionNotificationSource
    """Source of story reactions for which notifications are shown"""
    sound_id: int
    """Identifier of the notification sound to be played; 0 if sound is disabled"""
    show_preview: bool
    """True, if reaction sender and emoji must be displayed in notifications"""
