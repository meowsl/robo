from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("auth/", include("apps.api.auth.v1")),
    path("contentapp/", include("apps.api.contentapp.v1")),
]
