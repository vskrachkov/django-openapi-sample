from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework.schemas import get_schema_view


def swagger_ui(request: HttpRequest) -> HttpResponse:
    openapi_url = reverse("docs:openapi-schema")
    title = f"Swagger"
    return render(
        request,
        "docs/swagger.html",
        {
            "openapi_url": openapi_url,
            "title": title,
            "swagger_js_url": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.30.0/swagger-ui-bundle.js",
            "swagger_css_url": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.30.0/swagger-ui.css",
        },
    )


openapi_schema_view = get_schema_view(
    title="Users API", renderer_classes=[JSONOpenAPIRenderer]
)
