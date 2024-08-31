from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessRecipients(BaseType):
    """
    Describes private chats chosen for automatic interaction with a business
    """

    __type__: Literal["businessRecipients"] = "businessRecipients"

    chat_ids: list[int]
    """Identifiers of selected private chats"""
    excluded_chat_ids: list[int]
    """Identifiers of private chats that are always excluded; for businessConnectedBot only"""
    select_existing_chats: bool
    """True, if all existing private chats are selected"""
    select_new_chats: bool
    """True, if all new private chats are selected"""
    select_contacts: bool
    """True, if all private chats with contacts are selected"""
    select_non_contacts: bool
    """True, if all private chats with non-contacts are selected"""
    exclude_selected: bool
    """If true, then all private chats except the selected are chosen. Otherwise, only the selected chats are chosen"""
