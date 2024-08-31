from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteSavedOrderInfo(BaseMethod):
    """
    Deletes saved order information
    """

    __type__: Literal["deleteSavedOrderInfo"] = "deleteSavedOrderInfo"
    __returning_type__ = Ok
