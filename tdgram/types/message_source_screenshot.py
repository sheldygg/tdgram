from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSourceScreenshot(BaseType):
    """
    The message was screenshotted; the source must be used only if the message content was visible during the screenshot
    """

    __type__: Literal["messageSourceScreenshot"] = "messageSourceScreenshot"
