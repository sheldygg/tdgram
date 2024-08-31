from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import WebPageInstantView
from .base import BaseMethod


@dataclass(kw_only=True)
class GetWebPageInstantView(BaseMethod):
    """
    Returns an instant view version of a web page if available. Returns a 404 error if the web page has no instant view page
    """

    __type__: Literal["getWebPageInstantView"] = "getWebPageInstantView"
    __returning_type__ = WebPageInstantView

    url: str
    """The web page URL"""
    force_full: bool
    """Pass true to get full instant view for the web page"""
