import pytest

from django.core.cache import cache
from rest_framework.exceptions import ValidationError

from api.services import EmailCodeValidatorService


def test_email_code_valid(registration_data: dict[str, int | str]):
    cache.set(registration_data['email'], registration_data['code'])

    assert EmailCodeValidatorService(registration_data)() == registration_data


def test_email_code_invalid(registration_data: dict[str, int | str]):
    cache.set(registration_data['email'], registration_data['code'])
    registration_data['code'] = 654321

    with pytest.raises(ValidationError):
        EmailCodeValidatorService(registration_data)()
