from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PublicChatTypeHasUsername(BaseType):
    """
    The chat is public, because it has an active username
    """

    __type__: Literal["publicChatTypeHasUsername"] = "publicChatTypeHasUsername"
