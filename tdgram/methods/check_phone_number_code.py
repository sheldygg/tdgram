from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckPhoneNumberCode(BaseMethod):
    """
    Check the authentication code and completes the request for which the code was sent if appropriate
    """

    __type__: Literal["checkPhoneNumberCode"] = "checkPhoneNumberCode"
    __returning_type__ = Ok

    code: str
    """Authentication code to check"""
