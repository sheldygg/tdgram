from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSupportName(BaseMethod):
    """
    Returns localized name of the Telegram support user; for Telegram support only
    """

    __type__: Literal["getSupportName"] = "getSupportName"
    __returning_type__ = Text
