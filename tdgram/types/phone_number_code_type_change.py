from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PhoneNumberCodeTypeChange(BaseType):
    """
    Checks ownership of a new phone number to change the user's authentication phone number; for official Android and iOS applications only
    """

    __type__: Literal["phoneNumberCodeTypeChange"] = "phoneNumberCodeTypeChange"
