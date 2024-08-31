from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import OrderInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSavedOrderInfo(BaseMethod):
    """
    Returns saved order information. Returns a 404 error if there is no saved order information
    """

    __type__: Literal["getSavedOrderInfo"] = "getSavedOrderInfo"
    __returning_type__ = OrderInfo
