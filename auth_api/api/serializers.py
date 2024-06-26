from typing import Any

from rest_framework import serializers

from api.services import RegistrationValidatorService
from users.models import User


class CodeField(serializers.Serializer):
    """Code field with a range from 100000 to 999999."""
    code = serializers.IntegerField(min_value=100000, max_value=999999, write_only=True)


class RegistrationSerializer(serializers.ModelSerializer, CodeField):
    """Serializer for user registration."""
    password = serializers.CharField(
        write_only=True,
        help_text='Enter the password.',
        style={'input_type': 'password'},
    )
    confirm_password = serializers.CharField(
        write_only=True,
        help_text='Enter the password again.',
        style={'input_type': 'password'},
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'confirm_password', 'code')

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        return RegistrationValidatorService(attrs)()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for working with user objects. Except for registration."""
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')
