from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PersonalDetails


@dataclass(kw_only=True)
class InputPassportElementPersonalDetails(BaseType):
    """
    A Telegram Passport element to be saved containing the user's personal details
    """

    __type__: Literal["inputPassportElementPersonalDetails"] = (
        "inputPassportElementPersonalDetails"
    )

    personal_details: PersonalDetails
    """Personal details of the user"""
