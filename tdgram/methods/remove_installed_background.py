from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveInstalledBackground(BaseMethod):
    """
    Removes background from the list of installed backgrounds
    """

    __type__: Literal["removeInstalledBackground"] = "removeInstalledBackground"
    __returning_type__ = Ok

    background_id: int
    """The background identifier"""
