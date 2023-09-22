from django.db import models
from django.utils.translation import gettext_lazy as _

class PackagesInfo(models.Model):

  name = models.CharField(
    max_length=10,
    blank=False,
    verbose_name=_("Название пакета")
  )
  price = models.DecimalField(
    decimal_places=3,
    max_digits=10,
    blank=False,
    verbose_name=_("Цена пакета")
  )
  descript = models.CharField(
    max_length = 100,
    blank=False,
    verbose_name=_("Описание")
  )

  def __str__(self):
    return f'{self.name}'