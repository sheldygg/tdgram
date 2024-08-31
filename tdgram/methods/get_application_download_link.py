from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import HttpUrl
from .base import BaseMethod


@dataclass(kw_only=True)
class GetApplicationDownloadLink(BaseMethod):
    """
    Returns the link for downloading official Telegram application to be used when the current user invites friends to Telegram
    """

    __type__: Literal["getApplicationDownloadLink"] = "getApplicationDownloadLink"
    __returning_type__ = HttpUrl
