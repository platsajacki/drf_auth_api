from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

app_name = 'api'

urlpatterns = [
    path('', include('users.urls', namespace='users')),
    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/swagger/', SpectacularSwaggerView.as_view(url_name='api:schema')),
]
