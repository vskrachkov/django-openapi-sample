from django.urls import path, include

urlpatterns = [
    path("api/", include("users.urls", "users")),
    path("api/docs/", include("docs.urls", "docs")),
]
