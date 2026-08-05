from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/planetarium/", include("planetarium.urls", namespace="planetarium")),
    path("api/v1/user/", include("user.urls", namespace="user")),
    path("api-auth/", include("rest_framework.urls")),
]
