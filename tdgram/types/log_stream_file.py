from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LogStreamFile(BaseType):
    """
    The log is written to a file
    """

    __type__: Literal["logStreamFile"] = "logStreamFile"

    path: str
    """Path to the file to where the internal TDLib log will be written"""
    max_file_size: int
    """The maximum size of the file to where the internal TDLib log is written before the file will automatically be rotated, in bytes"""
    redirect_stderr: bool
    """Pass true to additionally redirect stderr to the log file. Ignored on Windows"""
