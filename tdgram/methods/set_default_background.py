from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Background, BackgroundType, InputBackground
from .base import BaseMethod


@dataclass(kw_only=True)
class SetDefaultBackground(BaseMethod):
    """
    Sets default background for chats; adds the background to the list of installed backgrounds
    """

    __type__: Literal["setDefaultBackground"] = "setDefaultBackground"
    __returning_type__ = Background

    background: InputBackground | None = None
    """The input background to use; pass null to create a new filled background"""
    type: BackgroundType | None = None
    """Background type; pass null to use the default type of the remote background; backgroundTypeChatTheme isn't supported"""
    for_dark_theme: bool
    """Pass true if the background is set for a dark theme"""
