from rest_framework import views, generics
from .serializers import TeachInfoAPI, ApplicationsAPI, PackagesInfoAPI
from apps.api.contentapp.models import TeachInfo, Applications, PackagesInfo

class TeachInfoAPIview(generics.ListAPIView):
  queryset = TeachInfo.objects.all()
  serializer_class = TeachInfoAPI

class ApplicationsCreateAPIview(generics.CreateAPIView):
  serializer_class = ApplicationsAPI

class PackagesInfoAPIview(generics.ListAPIView):
  queryset = PackagesInfo.objects.all()
  serializer_class = PackagesInfoAPI

