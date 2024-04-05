import pytest

from rest_framework.exceptions import ValidationError

from api.services import EmailCodeValidatorService


@pytest.mark.usefixtures('cache_email_code')
def test_email_code_valid(registration_data: dict[str, int | str]):
    assert EmailCodeValidatorService(registration_data)()


@pytest.mark.usefixtures('cache_email_code')
def test_email_code_invalid(registration_data: dict[str, int | str]):
    registration_data['code'] = 654321

    with pytest.raises(ValidationError):
        EmailCodeValidatorService(registration_data)()
