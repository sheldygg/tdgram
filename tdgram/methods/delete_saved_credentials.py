from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteSavedCredentials(BaseMethod):
    """
    Deletes saved credentials for all payment provider bots
    """

    __type__: Literal["deleteSavedCredentials"] = "deleteSavedCredentials"
    __returning_type__ = Ok
