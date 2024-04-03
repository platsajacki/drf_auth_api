import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.views import UserViewSet
from users.models import User

pytestmark = [pytest.mark.django_db]


def test_accessible_http_methods():
    assert sorted(UserViewSet.http_method_names) == ['delete', 'get', 'patch']


def test_unauthorized_users_dont_have_access_to_list(as_anon: APIClient):
    assert as_anon.get(reverse('api:users:user-list')).status_code == status.HTTP_401_UNAUTHORIZED


def test_unauthorized_users_dont_have_access_to_object(as_anon: APIClient, user: User):
    for method in [as_anon.get, as_anon.patch, as_anon.delete]:
        response = method(reverse('api:users:user-detail', kwargs={'pk': user.id}))
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
