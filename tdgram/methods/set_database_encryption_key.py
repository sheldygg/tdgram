from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetDatabaseEncryptionKey(BaseMethod):
    """
    Changes the database encryption key. Usually the encryption key is never changed and is stored in some OS keychain
    """

    __type__: Literal["setDatabaseEncryptionKey"] = "setDatabaseEncryptionKey"
    __returning_type__ = Ok

    new_encryption_key: bytes
    """New encryption key"""
