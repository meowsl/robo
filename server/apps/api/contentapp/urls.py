from django.urls import path
from .views import TeachInfoAPIview, ApplicationsAPIview, PackagesInfoAPIview

app_name = "contentapp"

urlpatterns = [
    path("teachers/", TeachInfoAPIview.as_view(), name="teachers"),
    path("applications/", ApplicationsAPIview.as_view(), name="applications"),
    path("packages/", PackagesInfoAPIview.as_view(), name="packages")
]
