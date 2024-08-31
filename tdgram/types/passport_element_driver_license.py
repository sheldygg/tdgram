from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import IdentityDocument


@dataclass(kw_only=True)
class PassportElementDriverLicense(BaseType):
    """
    A Telegram Passport element containing the user's driver license
    """

    __type__: Literal["passportElementDriverLicense"] = "passportElementDriverLicense"

    driver_license: IdentityDocument
    """Driver license"""
