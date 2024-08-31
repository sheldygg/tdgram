from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSourceHistoryPreview(BaseType):
    """
    The message is from chat, message thread or forum topic history preview
    """

    __type__: Literal["messageSourceHistoryPreview"] = "messageSourceHistoryPreview"
