from django.urls import path
from .views import TeachInfoAPIview, ApplicationsAPIview, PackagesInfoAPIview

app_name = "contentapp"

urlpatterns = [
    path("teachers/", TeachInfoAPIview.as_view(), name="teachs"),
    path("applics/", ApplicationsAPIview.as_view(), name="apps"),
    path("packages/", PackagesInfoAPIview.as_view(), name="packs")
]
