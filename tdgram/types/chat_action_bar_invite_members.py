from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionBarInviteMembers(BaseType):
    """
    The chat is a recently created group chat to which new members can be invited
    """

    __type__: Literal["chatActionBarInviteMembers"] = "chatActionBarInviteMembers"
