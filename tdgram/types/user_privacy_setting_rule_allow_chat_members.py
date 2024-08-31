from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingRuleAllowChatMembers(BaseType):
    """
    A rule to allow all members of certain specified basic groups and supergroups to doing something
    """

    __type__: Literal["userPrivacySettingRuleAllowChatMembers"] = (
        "userPrivacySettingRuleAllowChatMembers"
    )

    chat_ids: list[int]
    """The chat identifiers, total number of chats in all rules must not exceed 20"""
