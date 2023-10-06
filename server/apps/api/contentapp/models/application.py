from django.db import models
from django.utils.translation import gettext_lazy as _

class Applications(models.Model):
    name = models.CharField(_("Имя"), max_length=70, null=True, blank=False)
    phone = models.CharField(_("Телефон"), max_length=16, null=True, blank=False)
    email = models.EmailField(
        _("Email"), max_length=254, null=True, blank=False
    )

    def __str__(self):
        if self.name:
            return self.name
        return "Application - " + str(self.pk)

    class Meta:
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")