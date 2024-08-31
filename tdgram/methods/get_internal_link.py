from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import HttpUrl, InternalLinkType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetInternalLink(BaseMethod):
    """
    Returns an HTTPS or a tg: link with the given type. Can be called before authorization
    """

    __type__: Literal["getInternalLink"] = "getInternalLink"
    __returning_type__ = HttpUrl

    type: InternalLinkType
    """Expected type of the link"""
    is_http: bool
    """Pass true to create an HTTPS link (only available for some link types); pass false to create a tg: link"""
