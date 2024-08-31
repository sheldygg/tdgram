from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AuthorizationStateWaitOtherDeviceConfirmation(BaseType):
    """
    The user needs to confirm authorization on another logged in device by scanning a QR code with the provided link
    """

    __type__: Literal["authorizationStateWaitOtherDeviceConfirmation"] = (
        "authorizationStateWaitOtherDeviceConfirmation"
    )

    link: str
    """A tg:// URL for the QR code. The link will be updated frequently"""
