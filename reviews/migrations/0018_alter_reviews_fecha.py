# Generated by Django 4.2.3 on 2023-09-04 01:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0017_alter_reviews_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='fecha',
            field=models.CharField(default=datetime.date(2023, 9, 3), max_length=200),
        ),
    ]
