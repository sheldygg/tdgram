from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStoryNotificationSettingsExceptions(BaseMethod):
    """
    Returns the list of chats with non-default notification settings for stories
    """

    __type__: Literal["getStoryNotificationSettingsExceptions"] = (
        "getStoryNotificationSettingsExceptions"
    )
    __returning_type__ = Chats
