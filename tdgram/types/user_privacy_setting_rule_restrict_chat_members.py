from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UserPrivacySettingRuleRestrictChatMembers(BaseType):
    """
    A rule to restrict all members of specified basic groups and supergroups from doing something
    """

    __type__: Literal["userPrivacySettingRuleRestrictChatMembers"] = (
        "userPrivacySettingRuleRestrictChatMembers"
    )

    chat_ids: list[int]
    """The chat identifiers, total number of chats in all rules must not exceed 20"""
