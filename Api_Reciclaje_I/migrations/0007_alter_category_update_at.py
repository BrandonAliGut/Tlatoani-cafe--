# Generated by Django 4.2.4 on 2023-09-28 02:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_Reciclaje_I', '0006_alter_category_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='update_at',
            field=models.DateField(default=datetime.datetime(2023, 9, 27, 20, 52, 19, 188549)),
        ),
    ]