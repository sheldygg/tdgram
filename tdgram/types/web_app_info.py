from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class WebAppInfo(BaseType):
    """
    Contains information about a Web App
    """

    __type__: Literal["webAppInfo"] = "webAppInfo"

    launch_id: int
    """Unique identifier for the Web App launch"""
    url: str
    """A Web App URL to open in a web view"""
