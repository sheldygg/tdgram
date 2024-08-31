from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LinkPreviewTypeMessage(BaseType):
    """
    The link is a link to a text or a poll Telegram message
    """

    __type__: Literal["linkPreviewTypeMessage"] = "linkPreviewTypeMessage"
