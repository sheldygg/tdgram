from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import CallDiscardReason


@dataclass(kw_only=True)
class CallStateDiscarded(BaseType):
    """
    The call has ended successfully
    """

    __type__: Literal["callStateDiscarded"] = "callStateDiscarded"

    reason: CallDiscardReason
    """The reason why the call has ended"""
    need_rating: bool
    """True, if the call rating must be sent to the server"""
    need_debug_information: bool
    """True, if the call debug information must be sent to the server"""
    need_log: bool
    """True, if the call log must be sent to the server"""
