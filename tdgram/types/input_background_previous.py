from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputBackgroundPrevious(BaseType):
    """
    A background previously set in the chat; for chat backgrounds only
    """

    __type__: Literal["inputBackgroundPrevious"] = "inputBackgroundPrevious"

    message_id: int
    """Identifier of the message with the background"""
