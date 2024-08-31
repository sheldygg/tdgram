from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Updates
from .base import BaseMethod


@dataclass(kw_only=True)
class GetCurrentState(BaseMethod):
    """
    Returns all updates needed to restore current TDLib state, i.e. all actual updateAuthorizationState/updateUser/updateNewChat and others. This is especially useful if TDLib is run in a separate process. Can be called before initialization
    """

    __type__: Literal["getCurrentState"] = "getCurrentState"
    __returning_type__ = Updates
