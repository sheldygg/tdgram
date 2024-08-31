from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageScreenshotTaken(BaseType):
    """
    A screenshot of a message in the chat has been taken
    """

    __type__: Literal["messageScreenshotTaken"] = "messageScreenshotTaken"
