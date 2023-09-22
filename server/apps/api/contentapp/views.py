from django.shortcuts import render
from rest_framework import generics
from .v1.serializers import TeachInfoAPI, ApplicationsAPI, PackagesInfoAPI
from .models import TeachInfo, Applications, PackagesInfo

class TeachInfoAPIview(generics.ListAPIView):
  queryset = TeachInfo.objects.all()
  serializer_class = TeachInfoAPI


class ApplicationsAPIview(generics.ListAPIView):
  queryset = Applications.objects.all()
  serializer_class = ApplicationsAPI

class PackagesInfoAPIview(generics.ListAPIView):
  queryset = PackagesInfo.objects.all()
  serializer_class = PackagesInfoAPI

