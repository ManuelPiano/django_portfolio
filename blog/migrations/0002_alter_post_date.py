# Generated by Django 5.0.4 on 2024-05-06 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2024, 5, 6)),
        ),
    ]
