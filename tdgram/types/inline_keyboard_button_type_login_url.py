from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InlineKeyboardButtonTypeLoginUrl(BaseType):
    """
    A button that opens a specified URL and automatically authorize the current user by calling getLoginUrlInfo
    """

    __type__: Literal["inlineKeyboardButtonTypeLoginUrl"] = "inlineKeyboardButtonTypeLoginUrl"

    url: str
    """An HTTP URL to pass to getLoginUrlInfo"""
    id: int
    """Unique button identifier"""
    forward_text: str | None = None
    """If non-empty, new text of the button in forwarded messages"""
