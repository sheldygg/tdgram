from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ReportOption


@dataclass(kw_only=True)
class ReportStoryResultOptionRequired(BaseType):
    """
    The user must choose an option to report the story and repeat request with the chosen option
    """

    __type__: Literal["reportStoryResultOptionRequired"] = "reportStoryResultOptionRequired"

    title: str
    """Title for the option choice"""
    options: list[ReportOption]
    """List of available options"""
