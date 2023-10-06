from django.contrib import admin

from .models import TeachInfo, Applications, PackagesInfo

admin.site.register(TeachInfo)
admin.site.register(PackagesInfo)

@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
  list_display = ("name", "phone", "email")