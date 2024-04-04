import pytest

from django.core.cache import cache
from rest_framework.exceptions import ValidationError

from api.services import RegistrationValidatorService


def test_password_valid(registration_data: dict[str, int | str]):
    cache.set(registration_data['email'], registration_data['code'])

    assert RegistrationValidatorService(registration_data)()


def test_password_invalid(registration_data: dict[str, int | str]):
    cache.set(registration_data['email'], registration_data['code'])
    registration_data['confirm_password'] = 'test'

    with pytest.raises(ValidationError):
        RegistrationValidatorService(registration_data)()
