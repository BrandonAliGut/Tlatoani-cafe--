# Generated by Django 4.2.4 on 2023-09-27 01:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_Reciclaje_I', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='update_at',
            field=models.DateField(default=datetime.datetime(2023, 9, 26, 19, 56, 31, 501799)),
        ),
    ]
