from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContentappConfig(AppConfig):
    """Default app config"""

    name = "apps.api.contentapp"
    verbose_name = _("Contentapp")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
