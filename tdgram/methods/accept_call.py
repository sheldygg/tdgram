from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CallProtocol, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AcceptCall(BaseMethod):
    """
    Accepts an incoming call
    """

    __type__: Literal["acceptCall"] = "acceptCall"
    __returning_type__ = Ok

    call_id: int
    """Call identifier"""
    protocol: CallProtocol
    """The call protocols supported by the application"""
