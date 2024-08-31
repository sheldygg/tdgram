from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class HideContactCloseBirthdays(BaseMethod):
    """
    Hides the list of contacts that have close birthdays for 24 hours
    """

    __type__: Literal["hideContactCloseBirthdays"] = "hideContactCloseBirthdays"
    __returning_type__ = Ok
