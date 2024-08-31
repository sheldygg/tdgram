from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReportPhoneNumberCodeMissing(BaseMethod):
    """
    Reports that authentication code wasn't delivered via SMS to the specified phone number; for official mobile applications only
    """

    __type__: Literal["reportPhoneNumberCodeMissing"] = "reportPhoneNumberCodeMissing"
    __returning_type__ = Ok

    mobile_network_code: str
    """Current mobile network code"""
