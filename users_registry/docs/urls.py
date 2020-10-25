from django.urls import path

from . import views

app_name = "docs"

urlpatterns = [
    path("", views.swagger_ui, name="swagger-ui"),
    path("openapi_schema/", views.openapi_schema_view, name="openapi-schema"),
]
