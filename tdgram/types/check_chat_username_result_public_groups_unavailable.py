from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CheckChatUsernameResultPublicGroupsUnavailable(BaseType):
    """
    The user can't be a member of a public supergroup
    """

    __type__: Literal["checkChatUsernameResultPublicGroupsUnavailable"] = (
        "checkChatUsernameResultPublicGroupsUnavailable"
    )
