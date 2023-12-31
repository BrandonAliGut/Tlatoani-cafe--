# Generated by Django 4.2.4 on 2023-10-01 16:55

import cloudinary.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_Reciclaje_I', '0011_alter_category_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='Img_reciclaje_app'),
        ),
        migrations.AlterField(
            model_name='category',
            name='update_at',
            field=models.DateField(default=datetime.datetime(2023, 10, 1, 10, 55, 48, 936181)),
        ),
    ]
