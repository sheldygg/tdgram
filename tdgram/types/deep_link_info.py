from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class DeepLinkInfo(BaseType):
    """
    Contains information about a tg: deep link
    """

    __type__: Literal["deepLinkInfo"] = "deepLinkInfo"

    text: FormattedText
    """Text to be shown to the user"""
    need_update_application: bool
    """True, if the user must be asked to update the application"""
