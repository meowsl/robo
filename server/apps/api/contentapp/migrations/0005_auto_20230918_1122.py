# Generated by Django 3.2.16 on 2023-09-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0004_alter_expertinfo_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('study_place', models.TextField()),
                ('stude_facult', models.CharField(max_length=100)),
                ('study_spec', models.CharField(max_length=100)),
                ('study_form', models.CharField(blank=True, choices=[('INTERN', 'Очная'), ('DISTAN', 'Заочная')], default=None, max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='Positions',
        ),
    ]
