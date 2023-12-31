# Generated by Django 3.2.16 on 2023-10-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0016_alter_packagesinfo_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applications',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterField(
            model_name='applications',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='name',
            field=models.CharField(max_length=70, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='phone',
            field=models.CharField(max_length=16, null=True, verbose_name='Телефон'),
        ),
    ]
