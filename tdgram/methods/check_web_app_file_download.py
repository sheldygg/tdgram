from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckWebAppFileDownload(BaseMethod):
    """
    Checks whether a file can be downloaded and saved locally by Web App request
    """

    __type__: Literal["checkWebAppFileDownload"] = "checkWebAppFileDownload"
    __returning_type__ = Ok

    bot_user_id: int
    """Identifier of the bot, providing the Web App"""
    file_name: str
    """Name of the file"""
    url: str
    """URL of the file"""
