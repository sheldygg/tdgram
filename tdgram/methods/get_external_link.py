from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import HttpUrl
from .base import BaseMethod


@dataclass(kw_only=True)
class GetExternalLink(BaseMethod):
    """
    Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed
    """

    __type__: Literal["getExternalLink"] = "getExternalLink"
    __returning_type__ = HttpUrl

    link: str
    """The HTTP link"""
    allow_write_access: bool
    """Pass true if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages"""
