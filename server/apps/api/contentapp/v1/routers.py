from django.urls import path
from .views import TeachInfoAPIview, ApplicationsCreateAPIview, PackagesInfoAPIview

app_name = "contentapp"

urlpatterns = [
    path("teachers/", TeachInfoAPIview.as_view(), name="teachers"),
    path("applications/", ApplicationsCreateAPIview.as_view()),
    path("packages/", PackagesInfoAPIview.as_view(), name="packages")
]
