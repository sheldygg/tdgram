from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import NewChatPrivacySettings
from .base import BaseMethod


@dataclass(kw_only=True)
class GetNewChatPrivacySettings(BaseMethod):
    """
    Returns privacy settings for new chat creation
    """

    __type__: Literal["getNewChatPrivacySettings"] = "getNewChatPrivacySettings"
    __returning_type__ = NewChatPrivacySettings
