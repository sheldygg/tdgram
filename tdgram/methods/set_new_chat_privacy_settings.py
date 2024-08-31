from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import NewChatPrivacySettings, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetNewChatPrivacySettings(BaseMethod):
    """
    Changes privacy settings for new chat creation; can be used only if getOption('can_set_new_chat_privacy_settings')
    """

    __type__: Literal["setNewChatPrivacySettings"] = "setNewChatPrivacySettings"
    __returning_type__ = Ok

    settings: NewChatPrivacySettings
    """New settings"""
