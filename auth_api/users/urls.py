from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import RegistrationView, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='user')

app_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
    path('registration/', RegistrationView.as_view(), name='registration')
]
