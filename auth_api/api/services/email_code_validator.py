from dataclasses import dataclass
from typing import Any, Callable

from django.core.cache import cache
from rest_framework.exceptions import ValidationError

from api.services.base import BaseService


@dataclass
class EmailCodeValidatorService(BaseService):
    """Service for validating email codes stored in cache."""
    attrs: dict[str, Any]

    def validate_email_code(self) -> None:
        if cache.get(self.attrs['email']) != self.attrs['code']:
            return ValidationError('Invalid code.')

    def get_validators(self) -> list[Callable]:
        return super().get_validators() + [self.validate_email_code]

    def act(self) -> dict[str, Any]:
        return self.attrs
