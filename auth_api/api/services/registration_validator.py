from dataclasses import dataclass
from typing import Any, Callable

from rest_framework.exceptions import ValidationError

from api.services.email_code_validator import EmailCodeValidatorService


@dataclass
class RegistrationValidatorService(EmailCodeValidatorService):
    """Service for validating registration data."""
    attrs: dict[str, Any]

    def validate_password(self) -> None:
        if self.attrs['password'] != self.attrs.pop('confirm_password'):
            raise ValidationError('Passwords do not match.')

    def get_validators(self) -> list[Callable]:
        return super().get_validators() + [self.validate_password]
