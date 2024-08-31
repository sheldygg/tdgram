from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FormattedText, UserSupportInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class SetUserSupportInfo(BaseMethod):
    """
    Sets support information for the given user; for Telegram support only
    """

    __type__: Literal["setUserSupportInfo"] = "setUserSupportInfo"
    __returning_type__ = UserSupportInfo

    user_id: int
    """User identifier"""
    message: FormattedText
    """New information message"""
