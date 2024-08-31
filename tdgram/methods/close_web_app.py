from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CloseWebApp(BaseMethod):
    """
    Informs TDLib that a previously opened Web App was closed
    """

    __type__: Literal["closeWebApp"] = "closeWebApp"
    __returning_type__ = Ok

    web_app_launch_id: int
    """Identifier of Web App launch, received from openWebApp"""
