from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SendCallLog(BaseMethod):
    """
    Sends log file for a call to Telegram servers
    """

    __type__: Literal["sendCallLog"] = "sendCallLog"
    __returning_type__ = Ok

    call_id: int
    """Call identifier"""
    log_file: InputFile
    """Call log file. Only inputFileLocal and inputFileGenerated are supported"""
