from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CallId, CallProtocol
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateCall(BaseMethod):
    """
    Creates a new call
    """

    __type__: Literal["createCall"] = "createCall"
    __returning_type__ = CallId

    user_id: int
    """Identifier of the user to be called"""
    protocol: CallProtocol
    """The call protocols supported by the application"""
    is_video: bool
    """Pass true to create a video call"""
    group_call_id: int
    """Identifier of the group call to which the user will be added after exchanging private key via the call; pass 0 if none; currently, ignored"""
