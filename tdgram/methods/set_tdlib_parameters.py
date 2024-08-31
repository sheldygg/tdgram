from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetTdlibParameters(BaseMethod):
    """
    Sets the parameters for TDLib initialization. Works only when the current authorization state is authorizationStateWaitTdlibParameters
    """

    __type__: Literal["setTdlibParameters"] = "setTdlibParameters"
    __returning_type__ = Ok

    use_test_dc: bool
    """Pass true to use Telegram test environment instead of the production environment"""
    database_directory: str
    """The path to the directory for the persistent database; if empty, the current working directory will be used"""
    files_directory: str
    """The path to the directory for storing files; if empty, database_directory will be used"""
    database_encryption_key: bytes
    """Encryption key for the database. If the encryption key is invalid, then an error with code 401 will be returned"""
    use_file_database: bool
    """Pass true to keep information about downloaded and uploaded files between application restarts"""
    use_chat_info_database: bool
    """Pass true to keep cache of users, basic groups, supergroups, channels and secret chats between restarts. Implies use_file_database"""
    use_message_database: bool
    """Pass true to keep cache of chats and messages between restarts. Implies use_chat_info_database"""
    use_secret_chats: bool
    """Pass true to enable support for secret chats"""
    api_id: int
    """Application identifier for Telegram API access, which can be obtained at https://my.telegram.org"""
    api_hash: str
    """Application identifier hash for Telegram API access, which can be obtained at https://my.telegram.org"""
    system_language_code: str
    """IETF language tag of the user's operating system language; must be non-empty"""
    device_model: str
    """Model of the device the application is being run on; must be non-empty"""
    system_version: str
    """Version of the operating system the application is being run on. If empty, the version is automatically detected by TDLib"""
    application_version: str
    """Application version; must be non-empty"""
