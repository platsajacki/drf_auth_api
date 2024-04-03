from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView


class IsUserOrReadOnly(BasePermission):
    """Allow only the owner of the object to make changes."""
    def has_object_permission(self, request: Request, _: APIView, obj: AbstractBaseUser | AnonymousUser):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user
