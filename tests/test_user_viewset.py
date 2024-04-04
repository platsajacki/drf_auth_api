import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.serializers import UserSerializer
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


@pytest.mark.usefixtures('users')
def test_authorized_user_list(as_user: APIClient):
    response = as_user.get(reverse('api:users:user-list'))

    assert response.status_code == status.HTTP_200_OK
    assert response.data == UserSerializer(User.objects.all(), many=True).data


def test_authorized_user_detail(as_user: APIClient, user: User):
    response = as_user.get(reverse('api:users:user-detail', kwargs={'pk': user.id}))

    assert response.status_code == status.HTTP_200_OK
    assert response.data == UserSerializer(user).data


def test_another_user_cannot_update_object(as_user: APIClient, users: list[User]):
    response = as_user.patch(reverse('api:users:user-detail', kwargs={'pk': users[0].id}))

    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_another_user_cannot_delete_object(as_user: APIClient, users: list[User]):
    response = as_user.delete(reverse('api:users:user-detail', kwargs={'pk': users[0].id}))

    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_user_can_update_object(as_user: APIClient, user: User):
    response = as_user.patch(
        reverse('api:users:user-detail', kwargs={'pk': user.id}),
        data={'first_name': 'first_name'},
    )
    user.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK
    assert response.data == UserSerializer(user).data


def test_user_can_delete_object(as_user: APIClient, user: User):
    response = as_user.delete(reverse('api:users:user-detail', kwargs={'pk': user.id}))

    assert response.status_code == status.HTTP_204_NO_CONTENT
