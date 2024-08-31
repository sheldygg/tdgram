from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputIdentityDocument


@dataclass(kw_only=True)
class InputPassportElementDriverLicense(BaseType):
    """
    A Telegram Passport element to be saved containing the user's driver license
    """

    __type__: Literal["inputPassportElementDriverLicense"] = "inputPassportElementDriverLicense"

    driver_license: InputIdentityDocument
    """The driver license to be saved"""
