from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ReportReason
from .base import BaseMethod


@dataclass(kw_only=True)
class ReportStory(BaseMethod):
    """
    Reports a story to the Telegram moderators
    """

    __type__: Literal["reportStory"] = "reportStory"
    __returning_type__ = Ok

    story_sender_chat_id: int
    """The identifier of the sender of the story to report"""
    story_id: int
    """The identifier of the story to report"""
    reason: ReportReason
    """The reason for reporting the story"""
    text: str
    """Additional report details; 0-1024 characters"""
