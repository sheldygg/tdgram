from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteAllCallMessages(BaseMethod):
    """
    Deletes all call messages
    """

    __type__: Literal["deleteAllCallMessages"] = "deleteAllCallMessages"
    __returning_type__ = Ok

    revoke: bool
    """Pass true to delete the messages for all users"""
