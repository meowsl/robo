# Generated by Django 3.2.16 on 2023-10-06 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0017_auto_20231006_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packagesinfo',
            options={'verbose_name': 'Тариф', 'verbose_name_plural': 'Тарифы'},
        ),
        migrations.AlterModelOptions(
            name='teachinfo',
            options={'verbose_name': 'Тренер', 'verbose_name_plural': 'Тренеры'},
        ),
    ]