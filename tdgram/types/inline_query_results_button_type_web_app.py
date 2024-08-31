from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InlineQueryResultsButtonTypeWebApp(BaseType):
    """
    Describes the button that opens a Web App by calling getWebAppUrl
    """

    __type__: Literal["inlineQueryResultsButtonTypeWebApp"] = "inlineQueryResultsButtonTypeWebApp"

    url: str
    """An HTTP URL to pass to getWebAppUrl"""
