import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from users.models import User

pytestmark = [pytest.mark.django_db]


@pytest.mark.usefixtures('cache_email_code')
def test_unauthorized_user_can_create_account(as_anon: APIClient, registration_data: dict[str, int | str]):
    response = as_anon.post(
        reverse('api:users:registration'),
        data=registration_data,
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(email=registration_data['email']).exists()


@pytest.mark.usefixtures('cache_email_code')
def test_unauthorized_user_cannot_create_account_with_non_matching_password(
    as_anon: APIClient, registration_data: dict[str, int | str]
):
    registration_data['password'] = 'test12345678'
    response = as_anon.post(
        reverse('api:users:registration'),
        data=registration_data,
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert not User.objects.filter(email=registration_data['email']).exists()


@pytest.mark.usefixtures('cache_email_code')
def test_unauthorized_user_cannot_create_account_with_non_matching_code(
    as_anon: APIClient, registration_data: dict[str, int | str]
):
    registration_data['code'] = 555555
    response = as_anon.post(
        reverse('api:users:registration'),
        data=registration_data,
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert not User.objects.filter(email=registration_data['email']).exists()
