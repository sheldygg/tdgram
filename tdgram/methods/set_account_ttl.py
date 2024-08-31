from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AccountTtl, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetAccountTtl(BaseMethod):
    """
    Changes the period of inactivity after which the account of the current user will automatically be deleted
    """

    __type__: Literal["setAccountTtl"] = "setAccountTtl"
    __returning_type__ = Ok

    ttl: AccountTtl
    """New account TTL"""
