from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PersonalDetails


@dataclass(kw_only=True)
class PassportElementPersonalDetails(BaseType):
    """
    A Telegram Passport element containing the user's personal details
    """

    __type__: Literal["passportElementPersonalDetails"] = "passportElementPersonalDetails"

    personal_details: PersonalDetails
    """Personal details of the user"""
