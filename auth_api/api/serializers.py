from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for working with user objects. Except for registration."""
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')
