from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import IdentityDocument


@dataclass(kw_only=True)
class PassportElementPassport(BaseType):
    """
    A Telegram Passport element containing the user's passport
    """

    __type__: Literal["passportElementPassport"] = "passportElementPassport"

    passport: IdentityDocument
    """Passport"""
