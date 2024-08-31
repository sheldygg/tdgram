from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import WebApp


@dataclass(kw_only=True)
class FoundWebApp(BaseType):
    """
    Contains information about a Web App found by its short name
    """

    __type__: Literal["foundWebApp"] = "foundWebApp"

    web_app: WebApp
    """The Web App"""
    request_write_access: bool
    """True, if the user must be asked for the permission to the bot to send them messages"""
    skip_confirmation: bool
    """True, if there is no need to show an ordinary open URL confirmation before opening the Web App. The field must be ignored and confirmation must be shown anyway if the Web App link was hidden"""
