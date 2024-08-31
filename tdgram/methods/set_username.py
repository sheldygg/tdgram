from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetUsername(BaseMethod):
    """
    Changes the editable username of the current user
    """

    __type__: Literal["setUsername"] = "setUsername"
    __returning_type__ = Ok

    username: str
    """The new value of the username. Use an empty string to remove the username. The username can't be completely removed if there is another active or disabled username"""
