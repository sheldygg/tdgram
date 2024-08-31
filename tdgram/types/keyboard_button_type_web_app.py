from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class KeyboardButtonTypeWebApp(BaseType):
    """
    A button that opens a Web App by calling getWebAppUrl
    """

    __type__: Literal["keyboardButtonTypeWebApp"] = "keyboardButtonTypeWebApp"

    url: str
    """An HTTP URL to pass to getWebAppUrl"""
