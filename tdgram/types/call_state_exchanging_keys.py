from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallStateExchangingKeys(BaseType):
    """
    The call has been answered and encryption keys are being exchanged
    """

    __type__: Literal["callStateExchangingKeys"] = "callStateExchangingKeys"
