import pytest

from rest_framework.test import APIClient

from factory import person
from users.models import User


@pytest.fixture
def user() -> User:
    user = User.objects.create(
        email=person.email(unique=True), username=person.username()
    )
    user.set_password(person.password(length=20))
    return user


@pytest.fixture
def users():
    users = [
        User(email=person.email(unique=True), username=person.username())
        for _ in range(10)
    ]
    return User.objects.bulk_create(users)


@pytest.fixture
def as_anon() -> APIClient:
    return APIClient()


@pytest.fixture
def as_user(user: User) -> APIClient:
    as_user = APIClient()
    as_user.force_authenticate(user=user)
    return as_user
