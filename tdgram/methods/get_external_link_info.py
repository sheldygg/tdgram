from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LoginUrlInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetExternalLinkInfo(BaseMethod):
    """
    Returns information about an action to be done when the current user clicks an external link. Don't use this method for links from secret chats if link preview is disabled in secret chats
    """

    __type__: Literal["getExternalLinkInfo"] = "getExternalLinkInfo"
    __returning_type__ = LoginUrlInfo

    link: str
    """The link"""
