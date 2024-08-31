from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PersonalDocument


@dataclass(kw_only=True)
class PassportElementBankStatement(BaseType):
    """
    A Telegram Passport element containing the user's bank statement
    """

    __type__: Literal["passportElementBankStatement"] = "passportElementBankStatement"

    bank_statement: PersonalDocument
    """Bank statement"""
