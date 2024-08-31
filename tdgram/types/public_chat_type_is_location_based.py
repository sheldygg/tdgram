from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PublicChatTypeIsLocationBased(BaseType):
    """
    The chat is public, because it is a location-based supergroup
    """

    __type__: Literal["publicChatTypeIsLocationBased"] = "publicChatTypeIsLocationBased"
