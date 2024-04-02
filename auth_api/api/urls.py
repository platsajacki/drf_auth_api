from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import SimpleRouter

from api.views import UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='user')

app_name = 'api'

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('v1/docs/swagger/', SpectacularSwaggerView.as_view(url_name='api:schema')),
]
