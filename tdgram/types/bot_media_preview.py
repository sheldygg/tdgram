from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StoryContent


@dataclass(kw_only=True)
class BotMediaPreview(BaseType):
    """
    Describes media previews of a bot
    """

    __type__: Literal["botMediaPreview"] = "botMediaPreview"

    date: int
    """Point in time (Unix timestamp) when the preview was added or changed last time"""
    content: StoryContent
    """Content of the preview"""
