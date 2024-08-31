from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteAccount(BaseMethod):
    """
    Deletes the account of the current user, deleting all information associated with the user from the server. The phone number of the account can be used to create a new account.
    """

    __type__: Literal["deleteAccount"] = "deleteAccount"
    __returning_type__ = Ok

    reason: str
    """The reason why the account was deleted; optional"""
    password: str
    """The 2-step verification password of the current user. If the current user isn't authorized, then an empty string can be passed and account deletion can be canceled within one week"""
