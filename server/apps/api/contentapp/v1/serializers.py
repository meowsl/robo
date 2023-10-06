from rest_framework import serializers
from apps.api.contentapp.models import TeachInfo, Applications, PackagesInfo

class TeachInfoAPI(serializers.ModelSerializer):

  class Meta:
    model = TeachInfo
    fields = (
      "last_name",
      "first_name",
      "position",
      "date_start",
      "date_end",
      "study_place",
      "study_facult",
      "study_spec",
      "study_form",
      "photo"
    )

class ApplicationsAPI(serializers.ModelSerializer):

  class Meta:
    model = Applications
    fields = "__all__"

class PackagesInfoAPI(serializers.ModelSerializer):

  class Meta:
    model = PackagesInfo
    fields = (
      "name",
      "price",
      "descript"
    )
