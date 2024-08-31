from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetName(BaseMethod):
    """
    Changes the first and last name of the current user
    """

    __type__: Literal["setName"] = "setName"
    __returning_type__ = Ok

    first_name: str
    """The new value of the first name for the current user; 1-64 characters"""
    last_name: str
    """The new value of the optional last name for the current user; 0-64 characters"""
