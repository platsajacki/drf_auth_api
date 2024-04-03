from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsUserOrReadOnly
from api.schemas import extend_schema_user_view_set
from api.serializers import UserSerializer
from users.models import User


@extend_schema_user_view_set
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ['get', 'patch', 'delete']
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsUserOrReadOnly]
