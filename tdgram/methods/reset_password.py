from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ResetPasswordResult
from .base import BaseMethod


@dataclass(kw_only=True)
class ResetPassword(BaseMethod):
    """
    Removes 2-step verification password without previous password and access to recovery email address. The password can't be reset immediately and the request needs to be repeated after the specified time
    """

    __type__: Literal["resetPassword"] = "resetPassword"
    __returning_type__ = ResetPasswordResult
