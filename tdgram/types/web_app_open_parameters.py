from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ThemeParameters, WebAppOpenMode


@dataclass(kw_only=True)
class WebAppOpenParameters(BaseType):
    """
    Options to be used when a Web App is opened
    """

    __type__: Literal["webAppOpenParameters"] = "webAppOpenParameters"

    theme: ThemeParameters | None = None
    """Preferred Web App theme; pass null to use the default theme"""
    application_name: str
    """Short name of the current application; 0-64 English letters, digits, and underscores"""
    mode: WebAppOpenMode | None = None
    """The mode in which the Web App is opened; pass null to open in webAppOpenModeFullSize"""
