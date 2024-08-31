from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateWebAppMessageSent(BaseType):
    """
    A message was sent by an opened Web App, so the Web App needs to be closed
    """

    __type__: Literal["updateWebAppMessageSent"] = "updateWebAppMessageSent"

    web_app_launch_id: int
    """Identifier of Web App launch"""
