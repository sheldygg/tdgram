from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import TMeUrls
from .base import BaseMethod


@dataclass(kw_only=True)
class GetRecentlyVisitedTMeUrls(BaseMethod):
    """
    Returns t.me URLs recently visited by a newly registered user
    """

    __type__: Literal["getRecentlyVisitedTMeUrls"] = "getRecentlyVisitedTMeUrls"
    __returning_type__ = TMeUrls

    referrer: str
    """Google Play referrer to identify the user"""
