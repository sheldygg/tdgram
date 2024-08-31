from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputBusinessStartPage, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBusinessStartPage(BaseMethod):
    """
    Changes the business start page of the current user. Requires Telegram Business subscription
    """

    __type__: Literal["setBusinessStartPage"] = "setBusinessStartPage"
    __returning_type__ = Ok

    start_page: InputBusinessStartPage | None = None
    """The new start page of the business; pass null to remove custom start page"""
