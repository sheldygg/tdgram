from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import WebApp


@dataclass(kw_only=True)
class BotWriteAccessAllowReasonLaunchedWebApp(BaseType):
    """
    The user launched a Web App using getWebAppLinkUrl
    """

    __type__: Literal["botWriteAccessAllowReasonLaunchedWebApp"] = (
        "botWriteAccessAllowReasonLaunchedWebApp"
    )

    web_app: WebApp
    """Information about the Web App"""
