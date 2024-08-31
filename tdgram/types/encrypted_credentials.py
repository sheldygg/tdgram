from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EncryptedCredentials(BaseType):
    """
    Contains encrypted Telegram Passport data credentials
    """

    __type__: Literal["encryptedCredentials"] = "encryptedCredentials"

    data: bytes
    """The encrypted credentials"""
    hash: bytes
    """The decrypted data hash"""
    secret: bytes
    """Secret for data decryption, encrypted with the service's public key"""
