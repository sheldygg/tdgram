from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatAdministratorRights, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetDefaultGroupAdministratorRights(BaseMethod):
    """
    Sets default administrator rights for adding the bot to basic group and supergroup chats; for bots only
    """

    __type__: Literal["setDefaultGroupAdministratorRights"] = "setDefaultGroupAdministratorRights"
    __returning_type__ = Ok

    default_group_administrator_rights: ChatAdministratorRights | None = None
    """Default administrator rights for adding the bot to basic group and supergroup chats; pass null to remove default rights"""
