from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PassportElements
from .base import BaseMethod


@dataclass(kw_only=True)
class GetAllPassportElements(BaseMethod):
    """
    Returns all available Telegram Passport elements
    """

    __type__: Literal["getAllPassportElements"] = "getAllPassportElements"
    __returning_type__ = PassportElements

    password: str
    """The 2-step verification password of the current user"""
