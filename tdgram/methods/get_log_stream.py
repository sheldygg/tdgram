from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import LogStream
from .base import BaseMethod


@dataclass(kw_only=True)
class GetLogStream(BaseMethod):
    """
    Returns information about currently used log stream for internal logging of TDLib. Can be called synchronously
    """

    __type__: Literal["getLogStream"] = "getLogStream"
    __returning_type__ = LogStream
