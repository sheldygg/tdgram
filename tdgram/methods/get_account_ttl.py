from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AccountTtl
from .base import BaseMethod


@dataclass(kw_only=True)
class GetAccountTtl(BaseMethod):
    """
    Returns the period of inactivity after which the account of the current user will automatically be deleted
    """

    __type__: Literal["getAccountTtl"] = "getAccountTtl"
    __returning_type__ = AccountTtl
