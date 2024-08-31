from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SuggestedActionCheckPhoneNumber(BaseType):
    """
    Suggests the user to check whether authorization phone number is correct and change the phone number if it is inaccessible
    """

    __type__: Literal["suggestedActionCheckPhoneNumber"] = "suggestedActionCheckPhoneNumber"
