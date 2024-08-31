from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatMembersFilterAdministrators(BaseType):
    """
    Returns the owner and administrators
    """

    __type__: Literal["chatMembersFilterAdministrators"] = "chatMembersFilterAdministrators"
