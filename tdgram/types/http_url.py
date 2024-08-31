from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class HttpUrl(BaseType):
    """
    Contains an HTTP URL
    """

    __type__: Literal["httpUrl"] = "httpUrl"

    url: str
    """The URL"""
