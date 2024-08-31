from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReportAuthenticationCodeMissing(BaseMethod):
    """
    Reports that authentication code wasn't delivered via SMS; for official mobile applications only. Works only when the current authorization state is authorizationStateWaitCode
    """

    __type__: Literal["reportAuthenticationCodeMissing"] = "reportAuthenticationCodeMissing"
    __returning_type__ = Ok

    mobile_network_code: str
    """Current mobile network code"""
