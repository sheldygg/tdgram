from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ReportOption


@dataclass(kw_only=True)
class ReportChatResultOptionRequired(BaseType):
    """
    The user must choose an option to report the chat and repeat request with the chosen option
    """

    __type__: Literal["reportChatResultOptionRequired"] = "reportChatResultOptionRequired"

    title: str
    """Title for the option choice"""
    options: list[ReportOption]
    """List of available options"""
