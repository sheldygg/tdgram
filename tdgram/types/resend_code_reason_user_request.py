from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ResendCodeReasonUserRequest(BaseType):
    """
    The user requested to resend the code
    """

    __type__: Literal["resendCodeReasonUserRequest"] = "resendCodeReasonUserRequest"
