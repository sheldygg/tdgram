from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BackgroundType, HttpUrl
from .base import BaseMethod


@dataclass(kw_only=True)
class GetBackgroundUrl(BaseMethod):
    """
    Constructs a persistent HTTP URL for a background
    """

    __type__: Literal["getBackgroundUrl"] = "getBackgroundUrl"
    __returning_type__ = HttpUrl

    name: str
    """Background name"""
    type: BackgroundType
    """Background type; backgroundTypeChatTheme isn't supported"""
