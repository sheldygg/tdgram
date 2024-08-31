from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LogStream, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetLogStream(BaseMethod):
    """
    Sets new log stream for internal logging of TDLib. Can be called synchronously
    """

    __type__: Literal["setLogStream"] = "setLogStream"
    __returning_type__ = Ok

    log_stream: LogStream
    """New log stream"""
