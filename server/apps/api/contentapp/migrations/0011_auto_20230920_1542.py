# Generated by Django 3.2.16 on 2023-09-20 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0010_auto_20230920_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachinfo',
            name='position',
            field=models.CharField(choices=[('Преподаватель по программированию', 'Преподаватель по программированию'), ('Преподаватель по робототехнике', 'Преподаватель по робототехнике')], default=None, max_length=50, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='teachinfo',
            name='study_form',
            field=models.CharField(blank=True, choices=[('Очная', 'Очная'), ('Заочная', 'Заочная')], default=None, max_length=7, null=True, verbose_name='Форма обучения'),
        ),
    ]
