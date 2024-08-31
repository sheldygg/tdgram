from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatStatisticsAdministratorActionsInfo(BaseType):
    """
    Contains statistics about administrator actions done by a user
    """

    __type__: Literal["chatStatisticsAdministratorActionsInfo"] = (
        "chatStatisticsAdministratorActionsInfo"
    )

    user_id: int
    """Administrator user identifier"""
    deleted_message_count: int
    """Number of messages deleted by the administrator"""
    banned_user_count: int
    """Number of users banned by the administrator"""
    restricted_user_count: int
    """Number of users restricted by the administrator"""
