from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DisableProxy(BaseMethod):
    """
    Disables the currently enabled proxy. Can be called before authorization
    """

    __type__: Literal["disableProxy"] = "disableProxy"
    __returning_type__ = Ok
