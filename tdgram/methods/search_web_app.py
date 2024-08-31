from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundWebApp
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchWebApp(BaseMethod):
    """
    Returns information about a Web App by its short name. Returns a 404 error if the Web App is not found
    """

    __type__: Literal["searchWebApp"] = "searchWebApp"
    __returning_type__ = FoundWebApp

    bot_user_id: int
    """Identifier of the target bot"""
    web_app_short_name: str
    """Short name of the Web App"""
