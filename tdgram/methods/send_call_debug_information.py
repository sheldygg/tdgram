from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SendCallDebugInformation(BaseMethod):
    """
    Sends debug information for a call to Telegram servers
    """

    __type__: Literal["sendCallDebugInformation"] = "sendCallDebugInformation"
    __returning_type__ = Ok

    call_id: int
    """Call identifier"""
    debug_information: str
    """Debug information in application-specific format"""
