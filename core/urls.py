from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls', namespace='apis')),
    path('api/v1/', include('users.urls', namespace='user')),
    # OpenAPI 3 documentation with Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema",
        ),
        name="swagger-ui",
    ),
]
