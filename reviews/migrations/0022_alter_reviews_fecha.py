# Generated by Django 4.2.3 on 2023-09-04 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0021_alter_reviews_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='fecha',
            field=models.CharField(default='03-09-2023', max_length=200),
        ),
    ]
