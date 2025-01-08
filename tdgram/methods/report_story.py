from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ReportStoryResult
from .base import BaseMethod


@dataclass(kw_only=True)
class ReportStory(BaseMethod):
    """
    Reports a story to the Telegram moderators
    """

    __type__: Literal["reportStory"] = "reportStory"
    __returning_type__ = ReportStoryResult

    story_sender_chat_id: int
    """The identifier of the sender of the story to report"""
    story_id: int
    """The identifier of the story to report"""
    option_id: bytes
    """Option identifier chosen by the user; leave empty for the initial request"""
    text: str
    """Additional report details; 0-1024 characters; leave empty for the initial request"""
