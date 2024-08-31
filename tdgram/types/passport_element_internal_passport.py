from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import IdentityDocument


@dataclass(kw_only=True)
class PassportElementInternalPassport(BaseType):
    """
    A Telegram Passport element containing the user's internal passport
    """

    __type__: Literal["passportElementInternalPassport"] = "passportElementInternalPassport"

    internal_passport: IdentityDocument
    """Internal passport"""
