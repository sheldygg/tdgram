from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FirebaseAuthenticationSettingsAndroid(BaseType):
    """
    Settings for Firebase Authentication in the official Android application
    """

    __type__: Literal["firebaseAuthenticationSettingsAndroid"] = (
        "firebaseAuthenticationSettingsAndroid"
    )
