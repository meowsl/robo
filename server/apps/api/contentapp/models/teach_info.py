from django.db import models
from django.utils.translation import gettext_lazy as _
#from ckeditor.fields import RichTextFields

class TeachInfo(models.Model):

  STUDY_FORMAT = [
    ('Очная', 'Очная'),
    ('Заочная', 'Заочная')
  ]

  EXPERTS_POSITIONS = [
    ('Преподаватель по программированию', 'Преподаватель по программированию'),
    ('Преподаватель по робототехнике', 'Преподаватель по робототехнике')
  ]

  first_name = models.CharField(
      max_length=30,
      blank=False,
      verbose_name=_("Имя")
    )

  last_name = models.CharField(
      max_length=30,
      blank=False,
      verbose_name=_("Фамилия")
    )

  position = models.CharField(
      max_length=50,
      choices=EXPERTS_POSITIONS,
      default=None,
      verbose_name=_("Должность")
  )

  date_start = models.CharField(
      max_length=50,
      blank=True,
      null=True,
      verbose_name=_("Дата начала обучения")
    )

  date_end = models.CharField(
      max_length=50,
      blank=True,
      null=True,
      verbose_name=_("Дата окончания обучения")
    )

  study_place = models.TextField(
      blank=True,
      null=True,
      verbose_name=_("Место обучения")
    )

  study_facult = models.CharField(
      max_length=100,
      blank=True,
      null=True,
      verbose_name=_("Факультет")
    )

  study_spec = models.CharField(
      max_length=100,
      blank=True,
      null=True,
      verbose_name=_("Специальность")
    )

  study_form = models.CharField(
      max_length=7,
      choices=STUDY_FORMAT,
      blank=True,
      default=None,
      null=True,
      verbose_name=_("Форма обучения")
    )
  photo = models.ImageField(
      blank=False,
      null=True,
      upload_to=None,
      verbose_name=_("Фотография")
  )

  def __str__(self):
    return f'{self.last_name} {self.first_name[0]}. , {self.position}'

  class Meta:
    verbose_name = _("Тренер")
    verbose_name_plural = _("Тренеры")