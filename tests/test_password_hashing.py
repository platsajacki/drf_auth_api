import pytest

from django.contrib.auth.hashers import Argon2PasswordHasher, identify_hasher

from users.models import User

pytestmark = [pytest.mark.django_db]


def test_password_hash(user: User):
    """Argon2PasswordHasher should be used to hash passwords."""
    assert isinstance(identify_hasher(user.password), Argon2PasswordHasher)
