from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Birthdate, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBirthdate(BaseMethod):
    """
    Changes the birthdate of the current user
    """

    __type__: Literal["setBirthdate"] = "setBirthdate"
    __returning_type__ = Ok

    birthdate: Birthdate | None = None
    """The new value of the current user's birthdate; pass null to remove the birthdate"""
