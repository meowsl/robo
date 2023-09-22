from django.db import models
from django.utils.translation import gettext_lazy as _

class Applications(models.Model):

  name = models.CharField(
    max_length=30,
    blank=False,
    verbose_name=_("Имя участника")
  )
  phone = models.CharField(
    max_length=16,
    blank=False,
    verbose_name=_("Номер телефона")
  )
  email = models.CharField(
    max_length=100,
    blank=False,
    verbose_name=_("Почта")
  )

  def __str__(self):
    return f'{self.name}/{self.email}'