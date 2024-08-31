from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatAdministratorRights, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetDefaultChannelAdministratorRights(BaseMethod):
    """
    Sets default administrator rights for adding the bot to channel chats; for bots only
    """

    __type__: Literal["setDefaultChannelAdministratorRights"] = (
        "setDefaultChannelAdministratorRights"
    )
    __returning_type__ = Ok

    default_channel_administrator_rights: ChatAdministratorRights | None = None
    """Default administrator rights for adding the bot to channels; pass null to remove default rights"""
