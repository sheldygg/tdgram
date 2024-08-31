from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageFileTypeUnknown(BaseType):
    """
    The messages were exported from a chat of unknown type
    """

    __type__: Literal["messageFileTypeUnknown"] = "messageFileTypeUnknown"
