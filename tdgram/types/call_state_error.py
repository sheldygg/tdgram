from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Error


@dataclass(kw_only=True)
class CallStateError(BaseType):
    """
    The call has ended with an error
    """

    __type__: Literal["callStateError"] = "callStateError"

    error: Error
    """Error. An error with the code 4005000 will be returned if an outgoing call is missed because of an expired timeout"""
