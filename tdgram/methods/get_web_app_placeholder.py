from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Outline
from .base import BaseMethod


@dataclass(kw_only=True)
class GetWebAppPlaceholder(BaseMethod):
    """
    Returns a default placeholder for Web Apps of a bot; this is an offline request. Returns a 404 error if the placeholder isn't known
    """

    __type__: Literal["getWebAppPlaceholder"] = "getWebAppPlaceholder"
    __returning_type__ = Outline

    bot_user_id: int
    """Identifier of the target bot"""
