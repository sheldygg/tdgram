from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeBotCommand(BaseType):
    """
    A bot command, beginning with '/'
    """

    __type__: Literal["textEntityTypeBotCommand"] = "textEntityTypeBotCommand"
