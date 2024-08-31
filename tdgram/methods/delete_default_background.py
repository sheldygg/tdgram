from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteDefaultBackground(BaseMethod):
    """
    Deletes default background for chats
    """

    __type__: Literal["deleteDefaultBackground"] = "deleteDefaultBackground"
    __returning_type__ = Ok

    for_dark_theme: bool
    """Pass true if the background is deleted for a dark theme"""
