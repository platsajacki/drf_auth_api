import pytest

from factory import person
from users.models import User


@pytest.fixture
def user() -> User:
    user = User.objects.create(
        email=person.email(unique=True),
        username=person.username(),
    )
    user.set_password(person.password(length=20))
    return user
