from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CancelPasswordReset(BaseMethod):
    """
    Cancels reset of 2-step verification password. The method can be called if passwordState.pending_reset_date > 0
    """

    __type__: Literal["cancelPasswordReset"] = "cancelPasswordReset"
    __returning_type__ = Ok
