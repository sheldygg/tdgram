from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatSourceMtprotoProxy(BaseType):
    """
    The chat is sponsored by the user's MTProxy server
    """

    __type__: Literal["chatSourceMtprotoProxy"] = "chatSourceMtprotoProxy"
