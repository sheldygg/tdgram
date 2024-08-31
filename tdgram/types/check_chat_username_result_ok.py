from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CheckChatUsernameResultOk(BaseType):
    """
    The username can be set
    """

    __type__: Literal["checkChatUsernameResultOk"] = "checkChatUsernameResultOk"
